def get_qa_prompt(requirement):

    return f"""
Act as a Senior QA Engineer with expertise in Banking, Security Testing, Boundary Testing and Risk Analysis.

Requirement:
{requirement}

Generate the following in valid JSON format only.

{{
    "ba_questions": [],
    "test_scenarios": [],
    "positive_test_cases": [],
    "negative_test_cases": [],
    "boundary_test_cases": [],
    "risks": []
}}

Rules:

1. Return ONLY JSON.
2. Do not include markdown.
3. Do not use ```json.
4. Every section must contain multiple items.
5. Each test case should include:
   - id
   - description
   - steps
   - expected_result
"""