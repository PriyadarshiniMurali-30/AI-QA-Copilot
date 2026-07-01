import json
import ast
from groq import Groq
from config import GROQ_API_KEY
from utils import parse_llm_response


#client = Groq(api_key=GROQ_API_KEY)

import streamlit as st
from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


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

        return parse_llm_response(response_text)

    except Exception as e:
        return False, f"ERROR: {str(e)}"