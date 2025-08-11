from typing import Any, Dict, Optional
import logging
from app.ai.agent_graph import run_agent_graph

logger = logging.getLogger(__name__)

# Single orchestration entry point used by FastAPI
def answer_business_question(question: str, schema_context: str, output_format: str = "json", db_schema: Optional[str] = None) -> Dict[str, Any]:
    logger.debug(f"/ask received - question: {question}, output_format: {output_format}, db_schema: {db_schema}")
    result = run_agent_graph(question, schema_context, output_format, db_schema=db_schema)
    logger.debug(f"/ask result: {result}")
    return result