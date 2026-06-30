def get_qa_prompt(requirement):

    return f"""
You are a Senior QA Engineer with expertise in Banking Applications, Functional Testing, Security Testing, Boundary Testing and Risk Analysis.

Requirement:
{requirement}

Generate ONLY valid JSON.

Do NOT include:
- Markdown
- Triple backticks
- Explanations
- Notes
- Introductory text

Return exactly this JSON structure:

{{
  "ba_questions": [
    {{
      "id": "BAQ_001",
      "question": ""
    }}
  ],

  "test_scenarios": [
    {{
      "id": "TSC_001",
      "description": ""
    }}
  ],

  "positive_test_cases": [
    {{
      "id": "PTC_001",
      "description": "",
      "steps": [],
      "expected_result": ""
    }}
  ],

  "negative_test_cases": [
    {{
      "id": "NTC_001",
      "description": "",
      "steps": [],
      "expected_result": ""
    }}
  ],

  "boundary_test_cases": [
    {{
      "id": "BTC_001",
      "description": "",
      "steps": [],
      "expected_result": ""
    }}
  ],

  "risks": [
    {{
      "id": "RISK_001",
      "description": ""
    }}
  ]
}}

Rules:

1. Return ONLY valid JSON.
2. Use double quotes only.
3. Do not wrap the response inside ```json.
4. Generate at least:
   - 6 BA Questions
   - 6 Test Scenarios
   - 6 Positive Test Cases
   - 6 Negative Test Cases
   - 5 Boundary Test Cases
   - 5 Risks
5. Every ID must be unique.
6. Every step should be meaningful and detailed.
7. Expected results should be clear and verifiable.
8. Risks should focus on security, usability, business impact, compliance, and performance.
"""