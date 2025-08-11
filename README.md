<p align="center">
  <a href="https://ninestarsgroup.infinityfree.me/">
    <img src="logo.jpeg" alt="NineStarsGroup – ERP AI Agent" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Work with NineStarsGroup</strong><br/>
  <a href="mailto:groupofstars36145@gmail.com">groupofstars36145@gmail.com</a> ·
  <a href="https://ninestarsgroup.infinityfree.me/">Portfolio</a> ·
  <a href="https://www.linkedin.com/company/nine-stars-group/">LinkedIn</a>
</p>

## ERP (Enterprise Resource Planning) AI Agent Backend

FastAPI backend for an ERP AI Agent using LangGraph and LangChain. The agent answers business questions by retrieving focused schema/business context from Pinecone, validating against live PostgreSQL schema, generating secure SQL, optionally performing KPI calculations, and returning results in multiple formats.

### Architecture
- LangGraph flow
  - supervisor → schema_context → business_sql_agent → [calculation_agent → calculation_agent → …] → END
  - **Supervisor**: uses a domain-aware prompt to select the agent and extract compact retrieval keywords (index_terms) from the user question
  - **Schema Context**: retrieves relevant docs from Pinecone (table_overview, sample_query, business_note) filtered by `index_terms`, then introspects candidate tables from the live DB to build a compact prompt context
  - **Business SQL Agent**: generates SQL using focused context, executes it with read-only guard, timeout, single-statement enforcement, and row limit
  - **Calculation Agent**: optionally computes KPIs (growth, margin, conversion rate, ROI, etc.) on top of SQL results; supports iterative calculations via a task queue in graph state

- Tools and modules
  - `app/ai/tools/pinecone_schema_retriever.py`: Pinecone retrieval with metadata filters and keyword re-ranking
  - `app/ai/tools/pinecone_ingest.py`: simple ingestor to upsert schema docs into Pinecone
  - `app/ai/tools/db_introspector.py`: SQLAlchemy inspector for authoritative columns/keys
  - `app/ai/agents/business_sql_agent.py`: SQL generation + secure execution
  - `app/ai/agents/calculation_agent.py`: KPI calculations with LLM-assisted parsing
  - `app/ai/agent_graph.py`: graph definition and routing

### Requirements
- Python 3.10+
- PostgreSQL with a connection string that works with `psycopg` (v3)

```
pip install -r requirements.txt
```

### Environment variables
- `DATABASE_URL` (required): PostgreSQL URL. The code normalizes to `postgresql+psycopg://`.
  - Examples: `postgresql+psycopg://user:pass@host:5432/db` or `postgres://…` (auto-normalized)
- `OPENAI_API_KEY` (required): for LLM and embeddings
- `PINECONE_API_KEY` and `PINECONE_ENVIRONMENT` (optional but recommended): for schema/business-doc retrieval
- Optional overrides:
  - `PINECONE_SCHEMA_INDEX` (default `schema-index`)
  - `PINECONE_SCHEMA_NAMESPACE` (default none)
  - `SCHEMA_DOCS_FOLDER` (default `docs/schema`)

### Run the API
```
uvicorn app.main:app --reload
```

### Endpoint
- POST `/ask`
  - body: `{ "question": "…", "output_format": "json|text|excel|pdf" }`
  - returns JSON by default; Excel returns base64 content; PDF returns a stub unless you implement a real generator

### Secure SQL execution
- Read-only: `SET TRANSACTION READ ONLY`
- Timeout: `SET LOCAL statement_timeout = 10000` (10s)
- Single-statement enforced (no `;`)
- Deny-list covers mutating statements (INSERT/UPDATE/DELETE/ALTER/…)
- Result row limit (~1000) for safety

### Pinecone schema docs workflow
1) Generate JSON stubs for all tables
```
python scripts/generate_schema_jsons.py
```
This creates files under `docs/schema/<namespace>/<table>.json` with (columns omitted; DB introspection used at runtime):
```
{
  "table": "amzn_ads_sponsored_products",
  "domain": "amazon.ads",
  "overview": "",
  "business_notes": "",
  "index_terms": ["token1", "token2", …],  // used by supervisor + retriever for high-precision search
  "sample_queries": [
    { "name": "…", "sql": "SELECT …" }
  ]
}
```

2) Edit JSONs to add overview/business_notes/index_terms and sample_queries (no columns needed)
  - No need to include columns; live DB introspection provides authoritative schema

3) Ingest to Pinecone
```
python scripts/ingest_schema_docs.py
```
Env overrides let you choose the index and namespace:
```
PINECONE_SCHEMA_INDEX=schema-index \
PINECONE_SCHEMA_NAMESPACE=amazon.ads \
python scripts/ingest_schema_docs.py
```

### Namespaces in Pinecone
- Logical partitions inside one index; scope retrieval to a domain/tenant/environment for precision
- Examples: `amazon.ads`, `amazon.fba`, `amazon.reports`, `amazon.pnl`, `supply_chain`, `amazon.stage`

### Retrieval design
- Vector query uses supervisor-provided `index_terms` + metadata filter: `chunk_type in [table_overview, sample_query, business_note]`
- Reranking bonus for overlap between retrieved metadata.index_terms / table name and the supervisor’s `index_terms`
- Extract candidate `table` names from metadata, then introspect those tables live → compact context for SQL generation

### Calculation design
- Graph state (`AgentState`) carries:
  - `result` (SQL result), `calc_queue` (list of tasks)
- Business SQL node seeds `calc_queue` if the question implies KPI math
- Calculation node processes the queue, one task per turn, writing the final value back to `result`

### Extending
- Add new tools in `app/ai/tools/*` and wire new nodes in `app/ai/agent_graph.py`
- Add new output formats by extending `business_sql_agent.py` (e.g., CSV)
- Add guardrails (SQL validator/EXPLAIN node) if needed

### Troubleshooting
- Pinecone not configured: the system falls back to minimal context (graph still runs)
- `ModuleNotFoundError`: ensure `requirements.txt` is installed and Python version is 3.10+
- Database driver errors: the URL is normalized to `postgresql+psycopg://`; ensure `psycopg[binary]` is installed

### License
Copyright © 2025 NineStarsGroup. All rights reserved.

This repository is provided for demonstration and client evaluation purposes only. No license is granted to use, copy, modify, or distribute any part of this codebase without prior written consent from NineStarsGroup.

For commercial licensing, custom development, or collaboration inquiries, contact:
- Email: groupofstars36145@gmail.com
- Portfolio: https://ninestarsgroup.infinityfree.me/
 - LinkedIn: https://www.linkedin.com/company/nine-stars-group/


### Work with NineStarsGroup
Looking to build ERP and AI automation solutions? We take on projects end-to-end — from scoping and architecture to delivery and support.

- Email: groupofstars36145@gmail.com
- Portfolio: https://ninestarsgroup.infinityfree.me/
- LinkedIn: https://www.linkedin.com/company/nine-stars-group/

Reach out to discuss your project and how we can help.
