from typing import Any, Dict, List, Optional
import logging

try:
    from pinecone import Pinecone
except Exception:  # pragma: no cover
    Pinecone = None

from app.core.config import PINECONE_API_KEY


class SchemaRetrieverTool:
    name = "schema_retriever"
    description = "Retrieve relevant schema/business documentation chunks from Pinecone based on a question."

    def __init__(self, index_name: str):
        self.index_name = index_name
        self.logger = logging.getLogger(__name__)
        self._init_clients()

    def _init_clients(self) -> None:
        self.enabled = bool(Pinecone and PINECONE_API_KEY and self.index_name)
        if not self.enabled:
            self.index = None
            self.embeddings = None
            return
        try:
            pc = Pinecone(api_key=PINECONE_API_KEY)
            self.index = pc.Index(self.index_name)
        except Exception as e:
            self.logger.warning("Pinecone init/index failed: %s", e)
            self.enabled = False
            self.index = None
        # Using server-side embeddings and record search; no client-side embeddings
        self.embeddings = None

    def run(
        self,
        question: Optional[str] = None,
        namespace: Optional[str] = "default",
        top_k: int = 8,
        metadata_filter: Optional[Dict[str, Any]] = None,
        index_terms: Optional[List[str]] = None,
    ) -> List[Dict[str, Any]]:
        
        if not self.enabled or not self.index:
            return []
        try:
            query_text = " ".join(index_terms) if index_terms else (question or "")
            self.logger.debug(f"------------------ query_text: {query_text} ------------------")
            if not query_text:
                return []
            # Build server-side search query for records (text field is 'chunk_text')
            from pinecone.db_data.request_factory import SearchQuery
            sq = SearchQuery(inputs={"text": query_text}, top_k=top_k)
            # Optional rerank by 'chunk_text'
            res = self.index.search_records(namespace=namespace or "default", query=sq, rerank=None, fields=["*"])
            # Normalize response → hits list
            hits: List[Dict[str, Any]] = []
            # Prefer dict access first
            if isinstance(res, dict):
                result_block = res.get("result") or res
                hits = result_block.get("hits") or result_block.get("matches") or []
            else:
                result_block = getattr(res, "result", None) or res
                hits = getattr(result_block, "hits", None) or getattr(result_block, "matches", None) or []

            docs: List[Dict[str, Any]] = []
            for h in hits or []:
                # Each hit is a dict with keys like _id, _score, fields
                if not isinstance(h, dict):
                    # Try attribute-style
                    fields = getattr(h, "fields", {}) or {}
                    score = getattr(h, "_score", None) or getattr(h, "score", None)
                else:
                    fields = h.get("fields", {}) or {}
                    score = h.get("_score") or h.get("score")

                metadata = fields if isinstance(fields, dict) else {}
                table = metadata.get("table")
                domain = metadata.get("domain")
                # Synthesized minimal text from table + index_terms if not explicitly stored
                idx_terms = metadata.get("index_terms") or []
                chunk_text = (metadata.get("chunk_text") or "").strip()
                base_text = (
                    chunk_text
                    or ((table or "") + (" " + " ".join(idx_terms) if idx_terms else ""))
                ).strip()
                docs.append({
                    "score": score,
                    "text": base_text.strip(),
                    "table": table,
                    "domain": domain,
                    "metadata": metadata,
                })
            # self.logger.debug(f"------------------ docs: {docs} ------------------")    
            # Lightweight rerank by overlap with index_terms
            if index_terms:
                terms_set = {t.lower() for t in index_terms}
                def overlap_bonus(d: Dict[str, Any]) -> float:
                    md = d.get("metadata") or {}
                    bonus = 0.0
                    # table name overlap
                    tbl = (md.get("table") or "").lower()
                    if tbl and any(t in tbl for t in terms_set):
                        bonus += 0.15
                    # index_terms metadata overlap
                    meta_terms = md.get("index_terms") or []
                    if isinstance(meta_terms, list):
                        inter = terms_set.intersection({str(x).lower() for x in meta_terms})
                        bonus += 0.05 * len(inter)
                    return bonus
                for d in docs:
                    base = d.get("score") or 0.0
                    d["score"] = base + overlap_bonus(d)
                docs.sort(key=lambda x: x.get("score") or 0.0, reverse=True)
            return docs
        except Exception as e:
            self.logger.exception("------------------ Pinecone retrieval failed ------------------")
            return []

    @staticmethod
    def build_prompt_context(retrieved_docs: List[Dict[str, Any]], max_chars: int = 3000) -> str:
        chunks: List[str] = []
        size = 0
        for d in retrieved_docs:
            md = d.get("metadata") or {}
            chunk_type = md.get("chunk_type")
            table = md.get("table") or d.get("table") or ""
            block = ""
            if chunk_type == "table_overview":
                overview = (md.get("overview") or "").strip()
                notes = (md.get("business_notes") or "").strip()
                block = f"Table: {table}\nOverview: {overview}\nNotes: {notes}".strip()
            elif chunk_type == "sample_query":
                name = md.get("name") or "Sample"
                sql = (md.get("sql") or "").strip()
                sql = sql[:500]  # truncate to save tokens
                block = f"Sample Query: {name}\nSQL: {sql}"
            else:
                # Fallback to synthesized text (table + index_terms)
                block = d.get("text") or table

            if not block:
                continue
            add = block
            remaining = max_chars - size
            if len(add) > remaining:
                add = add[:remaining]
            chunks.append(add)
            size += len(add)
            if size >= max_chars:
                break
        return "\n\n".join(chunks)


