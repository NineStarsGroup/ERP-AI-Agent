from typing import List, Dict, Any, Optional
import logging
import uuid
import os

try:
    from pinecone import Pinecone, ServerlessSpec
except Exception:
    Pinecone = None

from app.core.config import PINECONE_API_KEY, PINECONE_CLOUD, PINECONE_REGION


class PineconeIngestor:
    def __init__(self, index_name: str):
        self.index_name = index_name
        self.logger = logging.getLogger(__name__)
        self._init()

    def _init(self):
        self.enabled = bool(Pinecone and PINECONE_API_KEY and self.index_name)
        if not self.enabled:
            self.index = None
            self.embedder = None
            return
        pc = Pinecone(api_key=PINECONE_API_KEY)
        # Force server-side embeddings only
        self.server_embed = True
        idx_names = pc.list_indexes().names()
        if self.index_name not in idx_names:
            try:
                if self.server_embed:
                    # Create server-embedded index using llama-text-embed-v2
                    pc.create_index_for_model(
                        name=self.index_name,
                        cloud=PINECONE_CLOUD or 'aws',
                        region=PINECONE_REGION or 'us-east-1',
                        embed={
                            "model": "llama-text-embed-v2",
                            "field_map": {"text": "chunk_text"}
                        }
                    )
                    logging.info(f"Server-side embedding index created for {self.index_name}")
                else:
                    pc.create_index(
                        name=self.index_name,
                        dimension=1536,
                        metric='cosine',
                        spec=ServerlessSpec(cloud=PINECONE_CLOUD or 'aws', region=PINECONE_REGION or 'us-east-1')
                    )
            except Exception as e:
                # Fallback to free-plan region
                self.logger.warning(
                    "Primary index creation failed for %s/%s, trying aws/us-east-1: %s",
                    PINECONE_CLOUD, PINECONE_REGION, e,
                )
                if self.server_embed:
                    pc.create_index_for_model(
                        name=self.index_name,
                        cloud='aws',
                        region='us-east-1',
                        embed={
                            "model": "llama-text-embed-v2",
                            "field_map": {"text": "chunk_text"}
                        }
                    )
                else:
                    pc.create_index(
                        name=self.index_name,
                        dimension=1536,
                        metric='cosine',
                        spec=ServerlessSpec(cloud='aws', region='us-east-1')
                    )
        self.index = pc.Index(self.index_name)
        # We only use server-side embeddings; no client embedder or local vectors

    def upsert_docs(
        self,
        docs: List[Dict[str, Any]],
        namespace: Optional[str] = None,
        batch_size: int = 64,
    ) -> Dict[str, Any]:
        """
        docs schema (recommended):
        [
          {
            # Minimal, normalized text; consider a short table signature or key terms here.
            # The heavy content (overview, sample queries, notes) can live in metadata.
            "text": "amzn_ads_sponsored_products product ads impressions clicks spend sales",
            "metadata": {
                "table": "amzn_ads_sponsored_products",
                "domain": "amazon.ads",
                "chunk_type": "table_overview|sample_query|business_note|column_overview",
                "overview": "... long table overview ...",
                "sample_queries": ["SELECT ...", "SELECT ..."],
                "business_notes": "... business context ...",
                "index_terms": ["sponsored products", "ads", "impressions", "clicks", "spend", "sales"],
                "version": "v1",
            }
          },
          ...
        ]
        """
        # Server-side embeddings only: require enabled and index
        if (not self.enabled) or (not self.index):
            return {"error": "Pinecone not configured"}
        records = []
        for d in docs:
            text = (d.get("text") or "").strip()
            if not text:
                continue
            metadata = _sanitize_metadata(d.get("metadata") or {})
            vid = str(metadata.get("id") or uuid.uuid4())
            # Server-side embeddings with model-mapped text field
            record = {"_id": vid, "chunk_text": text}
            # Attach sanitized metadata as top-level fields (allowed types only)
            for k, v in metadata.items():
                if k == "id":
                    continue
                record[k] = v
            records.append(record)
        if not records:
            return {"upserted": 0}
        upserted_total = 0
        ns = namespace or "default"
        for i in range(0, len(records), batch_size):
            batch = records[i:i+batch_size]
            self.index.upsert_records(namespace=ns, records=batch)
            upserted_total += len(batch)
        return {"upserted": upserted_total, "namespace": ns}


# Note: No client-side embedding utilities are needed when using server-side embeddings only.


def _sanitize_metadata(meta: Dict[str, Any]) -> Dict[str, Any]:
    """Sanitize metadata to satisfy Pinecone constraints.
    - Values must be: string, number, boolean, or list of strings
    - Convert complex fields (lists of dicts, dicts) to compact strings
    """
    sanitized: Dict[str, Any] = {}
    for k, v in (meta or {}).items():
        if v is None:
            continue
        if isinstance(v, (str, int, float, bool)):
            sanitized[k] = v
        elif isinstance(v, list):
            # If list of primitives, keep; else stringify compactly
            if all(isinstance(x, (str, int, float, bool)) for x in v):
                sanitized[k] = [str(x) if not isinstance(x, str) else x for x in v]
            else:
                # e.g., sample_queries is list of dicts -> store names only
                try:
                    names = []
                    for item in v:
                        if isinstance(item, dict):
                            name = item.get("name") or item.get("title") or "item"
                            names.append(str(name))
                        else:
                            names.append(str(item))
                    sanitized[k] = names
                except Exception:
                    sanitized[k] = [str(item) for item in v]
        elif isinstance(v, dict):
            # Flatten shallow dict to key:val string pairs
            try:
                parts = []
                for kk, vv in v.items():
                    if isinstance(vv, (str, int, float, bool)):
                        parts.append(f"{kk}:{vv}")
                sanitized[k] = ", ".join(parts)
            except Exception:
                sanitized[k] = str(v)
        else:
            sanitized[k] = str(v)
    return sanitized


