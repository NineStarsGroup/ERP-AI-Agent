from typing import Any, Dict

class FallbackAgent:
    def run(self, question: str, context: str = "", output_format: str = "json", **kwargs) -> Dict[str, Any]:
        return {
            "format": "text",
            "text": "Sorry, I couldn't understand or support your request. Please rephrase or contact support."
        }
