from typing import Dict, List
from sqlalchemy import inspect
from app.core.database import engine


class DBIntrospectionTool:
    name = "db_introspector"
    description = "Inspect live database to fetch exact columns, types, and constraints for candidate tables."

    def __init__(self):
        self.inspector = inspect(engine)

    def get_table_schema(self, table_name: str, schema: str = None) -> Dict:
        cols = self.inspector.get_columns(table_name, schema=schema)
        pks = self.inspector.get_pk_constraint(table_name, schema=schema)
        fks = self.inspector.get_foreign_keys(table_name, schema=schema)
        return {
            "table": table_name,
            "schema": schema,
            "columns": [{"name": c["name"], "type": str(c.get("type"))} for c in cols],
            "primary_key": pks.get("constrained_columns", []),
            "foreign_keys": [
                {"constrained_columns": fk.get("constrained_columns"), "referred_table": fk.get("referred_table"), "referred_columns": fk.get("referred_columns")}
                for fk in fks
            ],
        }

    def build_minimal_context(self, tables: List[Dict]) -> str:
        parts = []
        for t in tables:
            cols = ", ".join([f"{c['name']} {c['type']}" for c in t.get("columns", [])])
            pk = ", ".join(t.get("primary_key", []) or [])
            fk_parts = []
            for fk in t.get("foreign_keys", []) or []:
                fk_cols = ",".join(fk.get("constrained_columns") or [])
                ref = f"{fk.get('referred_table')}({','.join(fk.get('referred_columns') or [])})"
                fk_parts.append(f"FK({fk_cols}) -> {ref}")
            fk_line = "; ".join(fk_parts)
            parts.append(f"Table {t['table']}: {cols}\nPK: {pk}\n{fk_line}")
        return "\n\n".join(parts)


