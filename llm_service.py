from gemini_service import ask_gemini
from groq_service import ask_groq


def ask_llm(provider, prompt):

    if provider == "Gemini":
        return ask_gemini(prompt)

    elif provider == "Groq":
        return ask_groq(prompt)

    else:
        return False, "Unsupported LLM Provider."