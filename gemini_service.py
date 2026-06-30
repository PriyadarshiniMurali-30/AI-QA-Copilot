from google import genai
from google.genai.errors import ServerError
from config import GEMINI_API_KEY
import json
import ast

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt):
        
    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        try:
            qa_data = json.loads(response_text)
            return True, qa_data

        except json.JSONDecodeError:
            try:
                # Fallback: parse Python dictionary string
                qa_data = ast.literal_eval(response_text)
                return True, qa_data

            except Exception:
                return False, f"Invalid JSON returned by Gemini.\n\n{response_text}"

    except ServerError:
        return False, "ERROR: Gemini server is currently busy. Please try again later."

    except Exception as e:
        return False, f"ERROR: {str(e)}"


def review_test_cases(test_cases):

    review_prompt = f"""
Act as a QA Lead.

Review the following test artifacts.

Identify:

1. Missing Test Scenarios
2. Missing Boundary Test Cases
3. Missing Security Test Cases
4. Missing Risk Areas
5. Overall Coverage Percentage

Test Artifacts:

{test_cases}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=review_prompt
        )

        return response.text

    except Exception as e:
        return f"ERROR: {e}"