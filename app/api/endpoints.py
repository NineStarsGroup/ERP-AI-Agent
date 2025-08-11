from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict, Optional
from app.services.ai_agent_service import answer_business_question
from app.ai.schema.context import SCHEMA_CONTEXT

router = APIRouter()

class AskRequest(BaseModel):
    question: str
    output_format: Optional[str] = "json"
    db_schema: Optional[str] = None

@router.post("/ask")
def ask_endpoint(request: AskRequest) -> Dict[str, Any]:
    schema_context = SCHEMA_CONTEXT
    return answer_business_question(request.question, schema_context, request.output_format, request.db_schema)