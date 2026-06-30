import streamlit as st
import json

from llm_service import ask_llm
from excel_reader import read_requirements
from prompts import get_qa_prompt
from excel_reader import read_requirements
from excel_exporter import export_to_excel


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

provider = st.sidebar.selectbox(
    "🤖 Select AI Model",
    [
        "Groq",
        "Gemini"
    ]
)

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

               success, qa_data = ask_llm(provider, prompt)

            if not success:
                st.error(qa_data)

            else:

                # a_data = qa_data.replace("```json", "")
                # qa_data = qa_data.replace("```", "").strip() 

                try:

                    # data = json.loads(qa_data)

                    data = qa_data

                    st.success("QA Artifacts Generated Successfully!")

                    st.header("BA Questions")

                    for i, question in enumerate(data["ba_questions"], start=1):
                        st.write(f"{i}. {question['id']} - {question['question']}")
                

                    st.header("Test Scenarios")

                    for i, scenario in enumerate(data["test_scenarios"], start=1):
                        st.write(f"{i}. {scenario['id']} - {scenario['description']}")

                    st.header("Positive Test Cases")

                    for tc in data["positive_test_cases"]:

                        st.subheader(f"{tc['id']}")

                        st.write(f"**Description:** {tc['description']}")

                        st.write("**Steps:**")

                        for step in tc["steps"]:
                            st.write(f"- {step}")

                        st.write(f"**Expected Result:** {tc['expected_result']}")

                        st.divider()

                    st.header("Negative Test Cases")

                    for tc in data["negative_test_cases"]:

                        st.subheader(tc["id"])

                        st.write(f"**Description:** {tc['description']}")

                        st.write("**Steps:**")

                        for step in tc["steps"]:
                            st.write(f"- {step}")

                        st.write(f"**Expected Result:** {tc['expected_result']}")

                        st.divider()

                    st.header("Boundary Test Cases")

                    for tc in data["boundary_test_cases"]:

                        st.subheader(tc["id"])

                        st.write(f"**Description:** {tc['description']}")

                        st.write("**Steps:**")

                        for step in tc["steps"]:
                            st.write(f"- {step}")

                        st.write(f"**Expected Result:** {tc['expected_result']}")

                        st.divider()

                    st.header("Risks")

                    for i, risk in enumerate(data["risks"], start=1):
                        st.write(f"{i}. {risk['id']} - {risk['description']}")

                

                except Exception as e:

                    st.error(f"Error: {e}")
                    st.code(qa_data)

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

            progress_bar = st.progress(0)

            status_text = st.empty()

            results = []

            total = len(requirements)

            for index, requirement in enumerate(requirements, start=1):

                

                status_text.info(
                    f"Processing {index}/{total}\n\nCurrent Requirement: {requirement}"
                )

                prompt = get_qa_prompt(requirement)

                success, qa_data = ask_llm(provider, prompt)

                if success:

                    results.append({
                        "requirement": requirement,
                        "status": "Success",
                        "error": None,
                        "data": qa_data
                    })

                    st.success(f"✅ {requirement}")

                else:

                    results.append({
                        "requirement": requirement,
                        "status": "Failed",
                        "error": qa_data,
                        "data": None
                    })

                    st.error(f"❌ {requirement}")

                progress_bar.progress(index / total)

            status_text.success("Batch Processing Complete!")

            output_file = "output/QA_Report.xlsx"

            export_to_excel(results, output_file)

            st.success("✅ QA Report generated successfully!")

            with open(output_file, "rb") as file:

                st.download_button(
                    label="⬇ Download QA Report",
                    data=file,
                    file_name="QA_Report.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )