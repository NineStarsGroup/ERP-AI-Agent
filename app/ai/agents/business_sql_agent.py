from langchain_openai import ChatOpenAI
from typing import Any, Dict, List
from app.ai.tools.pdf_generator import PDFGeneratorTool
from app.ai.tools.excel_exporter import ExcelExporterTool
from sqlalchemy import text
from app.core.database import engine
import re
import logging

class BusinessSQLAgent:
    def __init__(self, llm: ChatOpenAI, pdf_tool: PDFGeneratorTool):
        self.llm = llm
        self.pdf_tool = pdf_tool
        self.excel_tool = ExcelExporterTool()

    def run(self, question: str, context: str = "", output_format: str = "json", **kwargs) -> Dict[str, Any]:
        sql = self.generate_sql(question, context)
        rows = self.execute_sql(sql)
        if output_format == "pdf":
            pdf = self.pdf_tool.run(str(rows))
            return {"format": "pdf", "pdf": pdf, "sql": sql}
        if output_format == "excel":
            excel = self.excel_tool.run(rows)
            return {"format": "excel", "excel": {"filename": excel.get("filename"), "size": excel.get("size")}, "sql": sql}
        if output_format == "text":
            return {"format": "text", "text": str(rows), "sql": sql}
        return {"format": "json", "result": rows, "sql": sql}

    def generate_sql(self, question: str, context: str) -> str:
        prompt = f"""
        You are a PostgreSQL SQL generator. Follow these rules strictly:
        - Use ONLY tables and columns present under the section "-- Live DB Schema (Authoritative) --" in the provided schema.
        - Do NOT invent columns or tables. If a desired field is missing, choose from available columns or compute from them.
        - Qualify columns with table aliases when multiple tables are used.
        - Prefer explicit JOIN conditions using keys that exist in the schema.
        - If you are unsure which column to use, pick the closest clearly-existing alternative from the schema.
        - Output a SINGLE SELECT (or WITH ... SELECT) statement. No comments or explanations.
        - If the question asks for a specific schema, the context may include a line like: SET search_path TO <schema>; Keep it at the very top if present.
        - Always include a LIMIT 200 unless the question explicitly asks for aggregates only.
        - Verify every selected column exists in the authoritative schema BEFORE outputting the final SQL.

        Provided Schema and Context:\n{context}
        Business question: {question}
        Return only the final SQL.
        """
        try:
            sql = self.llm.invoke(prompt).content.strip()
            return sql
        except Exception as e:
            return f"-- Error generating SQL: {e}"

    def execute_sql(self, sql: str) -> List[Dict[str, Any]]:
        """Execute a generated SQL query safely (read-only) and return rows.

        Protections:
        - Strips code fences and prose, extracts the SELECT statement only
        - Rejects multiple statements
        - Enforces read-only transaction in Postgres
        - Applies a statement timeout
        - Truncates result set to a safe maximum row count
        """
        logger = logging.getLogger(__name__)

        def clean_sql(generated: str) -> str:
            # Remove markdown fences and language hints
            cleaned = re.sub(r"^```[a-zA-Z]*\n|```$", "", generated.strip(), flags=re.MULTILINE)
            cleaned = cleaned.replace("`", "")
            # Extract from first SELECT/ WITH onwards
            match = re.search(r"\b(select|with)\b", cleaned, flags=re.IGNORECASE)
            if match:
                cleaned = cleaned[match.start():]
            # Remove trailing semicolons and whitespace
            cleaned = cleaned.strip().rstrip(";")
            return cleaned

        sql_clean = clean_sql(sql)

        # Basic denylist for dangerous keywords (best-effort)
        lowered = sql_clean.lower()
        forbidden = ["insert ", "update ", "delete ", "drop ", "alter ", "truncate ", "create ", "grant ", "revoke ", "vacuum ", "analyze "]
        if any(tok in lowered for tok in forbidden):
            return [{"error": "Only read-only SELECT queries are allowed", "sql": sql_clean}]

        # Disallow multiple statements via semicolons in the middle
        if ";" in sql_clean:
            return [{"error": "Multiple SQL statements are not allowed", "sql": sql_clean}]

        # Require SELECT/CTE
        if not (lowered.startswith("select") or lowered.startswith("with")):
            return [{"error": "Query must start with SELECT or WITH", "sql": sql_clean}]

        max_rows = 1000
        try:
            with engine.connect() as conn:
                trans = conn.begin()
                try:
                    # Read-only transaction and timeout (milliseconds)
                    conn.execute(text("SET TRANSACTION READ ONLY"))
                    conn.execute(text("SET LOCAL statement_timeout = 10000"))
                    # If the LLM included a SET search_path hint at top of SQL, allow it; otherwise ignore.
                    if sql_clean.lower().startswith("set search_path to"):
                        # Extract the SET line and run it separately then strip from sql_clean
                        first_newline = sql_clean.find("\n")
                        set_stmt = sql_clean[:first_newline] if first_newline != -1 else sql_clean
                        try:
                            conn.execute(text(set_stmt))
                        except Exception:
                            pass
                        sql_clean = sql_clean[first_newline+1:] if first_newline != -1 else sql_clean
                    result = conn.execute(text(sql_clean))
                    rows = [dict(r._mapping) for r in result]
                    # Truncate overly large result sets for safety
                    if len(rows) > max_rows:
                        rows = rows[:max_rows]
                    # Rollback read-only transaction explicitly
                    trans.rollback()
                except Exception:
                    trans.rollback()
                    raise
            return rows
        except Exception as e:
            logger.exception("SQL execution error")
            return [{"error": f"SQL execution failed: {e}", "sql": sql_clean}]
