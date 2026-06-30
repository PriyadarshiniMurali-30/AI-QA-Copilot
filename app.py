import streamlit as st
import json

from gemini_service import ask_gemini
from excel_reader import read_requirements
from prompts import get_qa_prompt
from excel_reader import read_requirements

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
tab1, tab2 = st.tabs([
    "📝 Single Requirement",
    "📂 Batch Processing"
])
# =====================================================
# SINGLE REQUIREMENT
# =====================================================
with tab1:
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

with tab2:

    st.subheader("📂 Batch Processing")

    uploaded_file = st.file_uploader(
        "Upload Requirements Excel",
        type=["xlsx"]
    )

    if uploaded_file:

        requirements, skipped_rows = read_requirements(uploaded_file)

        st.success("File uploaded successfully!")

        # Summary Cards
        col1, col2 = st.columns(2)

        with col1:
            st.metric("📋 Requirements", len(requirements))

        with col2:
            st.metric("⚠ Blank Rows Skipped", skipped_rows)

        st.info(f"📄 File: {uploaded_file.name}")

        st.divider()

        st.subheader("Preview")

        for requirement in requirements[:5]:
            st.write(f"• {requirement}")

        if len(requirements) > 5:
            st.info(f"...and {len(requirements)-5} more requirements.")

        st.divider()

        if st.button("🚀 Generate QA Report"):

            st.subheader("Processing Requirements")

            for index, requirement in enumerate(requirements, start=1):

                st.write(f"{index}. {requirement}")

            st.success("Processing Complete!")