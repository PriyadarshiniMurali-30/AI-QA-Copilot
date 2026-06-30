from google import genai
from google.genai.errors import ServerError
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt):

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except ServerError:
        return "ERROR: Gemini server is currently busy. Please try again later."


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