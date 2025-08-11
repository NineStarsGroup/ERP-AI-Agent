from langchain_openai import ChatOpenAI
from app.core.config import OPENAI_API_KEY
from app.ai.prompts.supervisor_routing_prompt import SUPERVISOR_ROUTING_PROMPT
import json

def llm_supervisor_route(question: str):
    """Returns tuple: (agent_name, index_terms: List[str])"""
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini", temperature=0)
    prompt = SUPERVISOR_ROUTING_PROMPT.format(question=question)
    raw = llm.invoke(prompt).content.strip()
    try:
        data = json.loads(raw)
        agent = str(data.get("agent", "fallback_agent")).strip()
        index_terms = data.get("index_terms") or []
        if not isinstance(index_terms, list):
            index_terms = []
        return agent, index_terms
    except Exception:
        # Fallback to simple keyword routing
        r = raw.lower()
        if "sql" in r or "query" in r or "table" in r or "report" in r:
            return "business_sql_agent", []
        if "calc" in r or "math" in r or "average" in r or "sum" in r:
            return "calculation_agent", []
        return "fallback_agent", []
