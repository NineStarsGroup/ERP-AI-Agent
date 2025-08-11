import logging
import re
from langgraph.graph import StateGraph, END
from app.ai.state import AgentState
from app.ai.supervisor import llm_supervisor_route
from app.ai.agents.business_sql_agent import BusinessSQLAgent
from app.ai.agents.calculation_agent import CalculationAgent
from app.ai.agents.fallback_agent import FallbackAgent
from app.ai.tools.pdf_generator import PDFGeneratorTool
from app.ai.tools.pinecone_schema_retriever import SchemaRetrieverTool
from app.ai.tools.db_introspector import DBIntrospectionTool
from langchain_openai import ChatOpenAI
from app.core.config import OPENAI_API_KEY
from typing import Dict, Any

logger = logging.getLogger(__name__)

# Instantiate tools and agents
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini", temperature=0)
pdf_tool = PDFGeneratorTool()
sql_agent = BusinessSQLAgent(llm, pdf_tool)
calc_agent = CalculationAgent()
fallback_agent = FallbackAgent()

schema_retriever = SchemaRetrieverTool(index_name="schema-index")
db_introspector = DBIntrospectionTool()

# Node functions must return partial state updates (dict)

def supervisor_node(state: AgentState) -> Dict[str, Any]:
    try:
        agent_choice, index_terms = llm_supervisor_route(state.question)
        next_agent = agent_choice
        debug = (state.debug or "") + f" | Routed to {next_agent}"
        # Extract index terms for Pinecone retrieval
        # logger.debug(f"Supervisor routing -> {next_agent}; index_terms={index_terms}")
        return {"next": next_agent, "debug": debug, "index_terms": index_terms}
    except Exception as e:
        logger.exception("Supervisor error")
        return {"next": "fallback_agent", "debug": (state.debug or "") + f" | Supervisor error: {e}"}

def schema_context_node(state: AgentState) -> Dict[str, Any]:
    try:
        # Step 1: Retrieve top-k docs (tables, sample queries, ERP notes) from Pinecone
        # Use filter to prefer docs tagged as table_overview or sample_query
        metadata_filter = {"chunk_type": {"$in": ["table_overview", "sample_query", "business_note"]}}
        # logger.debug(f"------------------ metadata_filter: {metadata_filter} ------------------")
        docs = schema_retriever.run(state.question, top_k=12, metadata_filter=metadata_filter, index_terms=getattr(state, 'index_terms', None))
        retrieved_context = SchemaRetrieverTool.build_prompt_context(docs, max_chars=2000)
        # logger.debug(f"------------------ retrieved_context: {retrieved_context} ------------------")   
        # Step 2: Extract candidate table names from metadata and sample queries
        candidate_tables = []
        seen = set()
        for d in docs:
            md = d.get("metadata") or {}
            t = (md.get("table") or d.get("table") or "").strip()
            if t and t not in seen:
                seen.add(t)
                candidate_tables.append(t)
        # logger.debug(f"------------------ candidate_tables: {candidate_tables} ------------------")
        # Step 3: Live DB introspection for authoritative columns/constraints
        introspected = []
        for t in candidate_tables:
            try:
                introspected.append(db_introspector.get_table_schema(t))
            except Exception:
                continue
        minimal_schema = db_introspector.build_minimal_context(introspected) if introspected else ""

        # Step 4: Build compact prompt context for SQLGenerator
        merged = "\n".join([
            "-- Retrieved Business Context (Tables, Sample Queries, ERP Notes) --",
            retrieved_context,
            "",
            "-- Live DB Schema (Authoritative) --",
            minimal_schema
        ])
        debug = (state.debug or "") + " | SchemaContext OK"
        return {"context": merged, "debug": debug, "next": "business_sql_agent"}
    except Exception as e:
        logger.exception("SchemaContext error")
        return {"debug": (state.debug or "") + f" | SchemaContext error: {e}", "next": "business_sql_agent"}

def business_sql_node(state: AgentState) -> Dict[str, Any]:
    try:
        logger.debug("BusinessSQLAgent start")
        result = sql_agent.run(state.question, state.context, state.output_format)
        logger.debug(f"BusinessSQLAgent result: {result}")
        # Heuristic: route to calculation agent if question suggests KPI math
        q = (state.question or "").lower()
        # Use word-boundary regex to avoid false positives like 'summary' matching 'sum'
        calc_terms = [
            "growth", "percent", "percentage", "margin", "roi", "turnover", "conversion",
            "average", "avg", "sum", "rate", "ratio", "change", "delta"
        ]
        pattern = r"\\b(" + "|".join(map(re.escape, calc_terms)) + r")\\b"
        needs_calc = bool(re.search(pattern, q))
        next_node = "calculation_agent" if needs_calc else "done"
        # Seed a simple calc_queue if needed (this can be enhanced to parse multiple ops)
        calc_queue = None
        if needs_calc:
            calc_queue = [{"operation_hint": "auto", "source": "sql_result"}]
        return {"result": result, "debug": (state.debug or "") + " | SQLAgent OK", "next": next_node, "calc_queue": calc_queue}
    except Exception as e:
        logger.exception("BusinessSQLAgent error")
        return {"result": {"error": str(e)}, "debug": (state.debug or "") + f" | SQLAgent error: {e}"}

def calculation_node(state: AgentState) -> Dict[str, Any]:
    try:
        logger.debug("CalculationAgent start")
        # Process a queue of calculations; for now, iterate until empty
        final_result = state.result
        calc_queue = list(state.calc_queue or [])
        calc_debug = []
        while calc_queue:
            task = calc_queue.pop(0)
            res = calc_agent.run(state.question, state.context, state.output_format, sql_result=final_result)
            calc_debug.append(res.get("debug") or "")
            # Merge result: prefer calculation output for 'result' when present
            if res and isinstance(res, dict) and ("result" in res or "text" in res):
                final_result = res
        logger.debug(f"CalculationAgent result: {final_result}")
        debug = (state.debug or "") + " | CalcAgent OK" + (" ".join(calc_debug) if calc_debug else "")
        return {"result": final_result, "debug": debug}
    except Exception as e:
        logger.exception("CalculationAgent error")
        return {"result": {"error": str(e)}, "debug": (state.debug or "") + f" | CalcAgent error: {e}"}

def fallback_node(state: AgentState) -> Dict[str, Any]:
    try:
        logger.debug("FallbackAgent start")
        result = fallback_agent.run(state.question, state.context, state.output_format)
        logger.debug(f"FallbackAgent result: {result}")
        return {"result": result, "debug": (state.debug or "") + " | FallbackAgent OK"}
    except Exception as e:
        logger.exception("FallbackAgent error")
        return {"result": {"error": str(e)}, "debug": (state.debug or "") + f" | FallbackAgent error: {e}"}

# Build the graph

def build_agent_graph():
    graph = StateGraph(AgentState)
    graph.add_node("supervisor", supervisor_node)
    graph.add_node("schema_context", schema_context_node)
    graph.add_node("business_sql_agent", business_sql_node)
    graph.add_node("calculation_agent", calculation_node)
    graph.add_node("fallback_agent", fallback_node)
    # Edges
    graph.add_conditional_edges(
        "supervisor",
        lambda s: s.next,
        {"business_sql_agent": "schema_context", "calculation_agent": "calculation_agent", "fallback_agent": "fallback_agent"}
    )
    # Always flow from schema_context to business_sql_agent
    graph.add_edge("schema_context", "business_sql_agent")
    # Conditionally flow from business_sql_agent to calculation_agent or END
    graph.add_conditional_edges(
        "business_sql_agent",
        lambda s: s.next,
        {"calculation_agent": "calculation_agent", "done": END}
    )
    graph.add_edge("calculation_agent", END)
    graph.add_edge("fallback_agent", END)
    graph.set_entry_point("supervisor")
    return graph.compile()

# Main entry point

def run_agent_graph(question: str, context: str = "", output_format: str = "json", db_schema: str = None):
    logger.debug(f"AgentGraph invoke → question: {question}, output_format: {output_format}")
    agent_graph = build_agent_graph()
    # Prepend a search_path hint for the LLM when a specific schema is requested
    context_with_schema = context
    if db_schema:
        context_with_schema = f"-- Use schema: {db_schema}\nSET search_path TO {db_schema};\n" + (context or "")
    initial_state = AgentState(question=question, context=context_with_schema, output_format=output_format)
    final_state = agent_graph.invoke(initial_state)
    # logger.debug(f"Final state: {final_state}")

    # Extract result and debug from either dict or AgentState
    if isinstance(final_state, dict):
        result = final_state.get("result")
        debug = final_state.get("debug", "")
    else:
        # Assume AgentState
        result = getattr(final_state, "result", None)
        debug = getattr(final_state, "debug", "")

    if isinstance(result, dict):
        payload = {**result, "debug": debug}
    else:
        payload = {"result": result, "debug": debug}

    logger.debug(f"Response payload: {payload}")
    return payload
