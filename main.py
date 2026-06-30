import json
from excel_exporter import export_test_artifacts
from gemini_service import ask_gemini

requirement = input("Enter requirement: ")

prompt = f"""
Act as a Senior QA Engineer.

Requirement:
{requirement}

Return ONLY valid JSON.

Format:

{{
  "ba_questions": [],
  "test_scenarios": [],
  "positive_test_cases": [],
  "negative_test_cases": [],
  "boundary_test_cases": [],
  "risks": []
}}

Return JSON only.
"""

result = ask_gemini(prompt)

#print("\nRAW RESPONSE\n")
#print(result)

# NEW CHECK
if result.startswith("ERROR:"):
    print("\nGemini request failed.")

else:

    try:

        clean_result = result.replace("```json", "")
        clean_result = clean_result.replace("```", "")
        clean_result = clean_result.strip()

        data = json.loads(clean_result)
        # print(type(data))


        export_test_artifacts(data)

        #print("\nBA QUESTIONS\n")

        #for question in data["ba_questions"]:
            #print("-", question)

    except json.JSONDecodeError:

        print("\nInvalid JSON returned by Gemini.")