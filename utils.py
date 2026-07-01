import json
import ast


def parse_llm_response(response_text):
    """
    Parses an LLM response into a Python dictionary.
    Supports:
    - Valid JSON
    - Python dictionary strings
    - Markdown wrapped JSON
    """

    response_text = response_text.replace("```json", "")
    response_text = response_text.replace("```", "").strip()

    try:
        return True, json.loads(response_text)

    except json.JSONDecodeError:

        try:
            return True, ast.literal_eval(response_text)

        except Exception:
            return False, f"Invalid JSON returned by the model.\n\n{response_text}"