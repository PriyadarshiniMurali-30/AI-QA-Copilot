import streamlit as st
import json

from gemini_service import ask_gemini
from excel_reader import read_requirements
from prompts import get_qa_prompt

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI QA Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI QA Copilot")
st.write("Generate QA artifacts using AI")

# =====================================================
# SINGLE REQUIREMENT
# =====================================================

st.header("📝 Single Requirement")

requirement = st.text_area(
    "Enter Requirement",
    height=120,
    placeholder="Example: User should login using email and password"
)

if st.button("🚀 Generate QA Artifacts"):

    if requirement.strip() == "":
        st.warning("Please enter a requirement.")

    else:

        prompt = get_qa_prompt(requirement)


        with st.spinner("Generating QA Artifacts..."):

            result = ask_gemini(prompt)

        if result.startswith("ERROR:"):
            st.error(result)

        else:

            result = result.replace("```json", "")
            result = result.replace("```", "").strip()

            try:

                data = json.loads(result)

                st.success("QA Artifacts Generated Successfully!")

                st.header("BA Questions")

                for i, question in enumerate(data["ba_questions"], start=1):
                    st.write(f"{i}. {question}")

                st.header("Test Scenarios")

                for i, scenario in enumerate(data["test_scenarios"], start=1):
                    st.write(f"{i}. {scenario}")

                st.header("Positive Test Cases")

                for i, test in enumerate(data["positive_test_cases"], start=1):
                    st.write(f"{i}. {test}")

                st.header("Negative Test Cases")

                for i, test in enumerate(data["negative_test_cases"], start=1):
                    st.write(f"{i}. {test}")

                st.header("Boundary Test Cases")

                for i, test in enumerate(data["boundary_test_cases"], start=1):
                    st.write(f"{i}. {test}")

                st.header("Risks")

                for i, risk in enumerate(data["risks"], start=1):
                    st.write(f"{i}. {risk}")

            except Exception:
                st.error("Invalid JSON returned by Gemini.")
                st.code(result)

# =====================================================
# BATCH PROCESSING
# =====================================================

st.divider()

st.header("📂 Batch Processing")

uploaded_file = st.file_uploader(
    "Upload Requirements Excel",
    type=["xlsx"]
)

if uploaded_file is not None:

    try:

        requirements = read_requirements(uploaded_file)

        st.success(f"Loaded {len(requirements)} requirements.")

        st.subheader("Preview")

        for i, req in enumerate(requirements, start=1):
            st.write(f"{i}. {req}")

        if st.button("🚀 Process All"):

            st.info(
                "Batch Processing will be implemented in the next step."
            )

    except Exception as e:

        st.error(f"Unable to read Excel file.\n\n{e}")