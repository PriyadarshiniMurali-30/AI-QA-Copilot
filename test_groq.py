from groq_service import ask_groq

prompt = """
Return ONLY this JSON.

{
    "message": "Hello"
}
"""

success, data = ask_groq(prompt)

print(success)
print(data)