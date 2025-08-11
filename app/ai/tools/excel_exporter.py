from typing import Any, Dict, List
import io
import pandas as pd
import base64

class ExcelExporterTool:
    name = "excel_exporter"
    description = "Export tabular data (list of dicts) to an Excel file (in-memory)."

    def run(self, rows: List[Dict[str, Any]], sheet_name: str = "Sheet1") -> Dict[str, Any]:
        if not isinstance(rows, list) or not rows:
            return {"error": "No rows to export"}
        df = pd.DataFrame(rows)
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name=sheet_name)
        buffer.seek(0)
        b = buffer.getvalue()
        # Return JSON-serializable descriptor
        return {"filename": f"export_{sheet_name}.xlsx", "content_base64": base64.b64encode(b).decode("utf-8"), "size": len(b)}

