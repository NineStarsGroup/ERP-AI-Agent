from pydantic import BaseModel
from typing import Any, Optional, List, Dict

class AgentState(BaseModel):
    question: str
    context: Optional[str] = ""
    output_format: Optional[str] = "json"
    result: Optional[Any] = None
    next: Optional[str] = None
    debug: Optional[str] = ""
    # Supervisor-extracted retrieval terms for Pinecone
    index_terms: Optional[List[str]] = None
    # Iterative calculation support
    calc_queue: Optional[List[Dict[str, Any]]] = None
