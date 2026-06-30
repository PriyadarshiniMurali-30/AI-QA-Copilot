import json
import ast
from groq import Groq
from config import GROQ_API_KEY


client = Groq(api_key=GROQ_API_KEY)


def ask_groq(prompt):

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        response_text = response.choices[0].message.content.strip()

        # Remove markdown if present
        response_text = response_text.replace("```json", "")
        response_text = response_text.replace("```", "").strip()

        try:
            qa_data = json.loads(response_text)
            return True, qa_data

        except json.JSONDecodeError:
            try:
                # Fallback: parse Python dictionary string
                qa_data = ast.literal_eval(response_text)
                return True, qa_data

            except Exception:
                return False, f"Invalid JSON returned by Groq.\n\n{response_text}"

    except Exception as e:

        return False, f"ERROR: {str(e)}"