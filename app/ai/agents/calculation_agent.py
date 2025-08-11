from typing import Any, Dict, Optional
import re
from langchain_openai import ChatOpenAI
from app.core.config import OPENAI_API_KEY

class CalculationAgent:
    def __init__(self):
        self.llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini", temperature=0)
        self.tools = {
            "sum": self._sum,
            "average": self._average,
            "min": self._min,
            "max": self._max,
            "count": self._count,
            "growth_rate": self._growth_rate,
            "percent_change": self._percent_change,
            "inventory_turnover": self._inventory_turnover,
            "gross_margin": self._gross_margin,
            "net_profit": self._net_profit,
            "cogs": self._cogs,
            "roi": self._roi,
            "conversion_rate": self._conversion_rate,
        }

    def run(self, question: str, context: str = "", output_format: str = "json", sql_result: Optional[Any] = None, **kwargs) -> Dict[str, Any]:
        """
        Use LLM to extract calculation intent and numbers, then run the appropriate calculation tool.
        Supports ERP metrics: sum, average, min, max, count, growth_rate, percent_change, inventory_turnover, gross_margin, net_profit, cogs, roi, conversion_rate.
        """
        try:
            prompt = f"""
            You are an ERP calculation agent. Given the user question and (optional) SQL result, extract the calculation type (operation) and numbers needed. Supported operations: {list(self.tools.keys())}. Return a JSON with 'operation' and 'numbers' (list or dict as needed).
            User question: {question}
            SQL result: {sql_result}
            """
            llm_response = self.llm.invoke(prompt).content.strip()
            import json
            try:
                parsed = json.loads(llm_response)
                operation = parsed.get("operation")
                numbers = parsed.get("numbers")
            except Exception:
                # Fallback: try to extract numbers and guess operation
                operation = self._guess_operation(question)
                numbers = [float(n) for n in re.findall(r"[-+]?[0-9]*\.?[0-9]+", question)]
            if not operation or operation not in self.tools:
                return {"error": f"Unsupported or missing operation: {operation}", "debug": llm_response}
            if not numbers:
                return {"error": "No numbers found for calculation.", "debug": llm_response}
            result = self.tools[operation](numbers)
            if output_format == "text":
                return {"format": "text", "text": f"{operation.title()}: {result}"}
            return {"format": "json", "result": result, "operation": operation, "numbers": numbers, "debug": llm_response}
        except Exception as e:
            return {"error": str(e)}

    def _guess_operation(self, question: str) -> Optional[str]:
        q = question.lower()
        for op in self.tools:
            if op.replace('_', ' ') in q or op in q:
                return op
        return None

    def _sum(self, numbers):
        return sum(numbers)
    def _average(self, numbers):
        return sum(numbers) / len(numbers) if numbers else None
    def _min(self, numbers):
        return min(numbers) if numbers else None
    def _max(self, numbers):
        return max(numbers) if numbers else None
    def _count(self, numbers):
        return len(numbers)
    def _growth_rate(self, numbers):
        # Expects [old_value, new_value]
        if len(numbers) < 2: return None
        old, new = numbers[0], numbers[1]
        return ((new - old) / old) * 100 if old != 0 else None
    def _percent_change(self, numbers):
        # Expects [old_value, new_value]
        return self._growth_rate(numbers)
    def _inventory_turnover(self, numbers):
        # Expects [cost_of_goods_sold, average_inventory]
        if len(numbers) < 2: return None
        cogs, avg_inv = numbers[0], numbers[1]
        return cogs / avg_inv if avg_inv != 0 else None
    def _gross_margin(self, numbers):
        # Expects [revenue, cogs]
        if len(numbers) < 2: return None
        revenue, cogs = numbers[0], numbers[1]
        return ((revenue - cogs) / revenue) * 100 if revenue != 0 else None
    def _net_profit(self, numbers):
        # Expects [revenue, cogs, expenses]
        if len(numbers) < 3: return None
        revenue, cogs, expenses = numbers[0], numbers[1], numbers[2]
        return revenue - cogs - expenses
    def _cogs(self, numbers):
        # Expects [beginning_inventory, purchases, ending_inventory]
        if len(numbers) < 3: return None
        begin_inv, purchases, end_inv = numbers[0], numbers[1], numbers[2]
        return begin_inv + purchases - end_inv
    def _roi(self, numbers):
        # Expects [gain_from_investment, cost_of_investment]
        if len(numbers) < 2: return None
        gain, cost = numbers[0], numbers[1]
        return ((gain - cost) / cost) * 100 if cost != 0 else None
    def _conversion_rate(self, numbers):
        # Expects [conversions, total_visitors]
        if len(numbers) < 2: return None
        conversions, visitors = numbers[0], numbers[1]
        return (conversions / visitors) * 100 if visitors != 0 else None
