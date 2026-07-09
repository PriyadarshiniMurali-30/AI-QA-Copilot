# 🤖 AI QA Copilot

AI QA Copilot is an AI-powered web application that helps QA Engineers generate software testing artifacts from requirements using Large Language Models (LLMs).

The application supports both **Single Requirement** and **Batch Requirement** processing, allowing users to automatically generate:

- Business Analyst Questions
- Test Scenarios
- Positive Test Cases
- Negative Test Cases
- Boundary Test Cases
- Risk Analysis

The generated artifacts can also be exported into a structured Excel report.

---

## 🚀 Live Demo

🔗 https://ai-app-q.streamlit.app/

---


## ✨ Features

### 📝 Single Requirement Processing

- Generate QA artifacts from a single requirement
- Supports multiple AI providers
- Clean and structured output
- Download generated report as Excel

### 📂 Batch Requirement Processing

- Upload Excel containing multiple requirements
- Automatically processes each requirement
- Progress bar showing processing status
- Generates a consolidated Excel report

### 🤖 Multiple AI Models

Supports:

- Gemini
- Groq (Llama 3.3 70B)

Easy to extend for additional LLM providers.

### 📊 Excel Report Generation

Automatically generates professional Excel reports containing:

- Summary
- BA Questions
- Test Scenarios
- Positive Test Cases
- Negative Test Cases
- Boundary Test Cases
- Risks

---

## 🛠 Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### AI Models

- Google Gemini
- Groq (Llama 3.3 70B)

### Libraries

- openpyxl
- streamlit
- google-genai
- groq

---

## 📂 Project Structure

```text
AI-QA-Copilot/
│
├── app.py
├── prompts.py
├── llm_service.py
├── gemini_service.py
├── groq_service.py
├── excel_reader.py
├── excel_exporter.py
├── config.py
├── requirements.txt
├── README.md

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/AI-QA-Copilot.git
cd AI-QA-Copilot
```

### Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Keys

This application supports two AI providers:

- Google Gemini
- Groq (Llama 3.3 70B)

### Local Development

Create a `.env` file in the project root directory and add your API keys:

```text
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

> **Note:** If you're using a `config.py` file instead of a `.env` file, configure your API keys there accordingly.

### Streamlit Cloud Deployment

For deployment on Streamlit Cloud:

1. Open your deployed app.
2. Click **Manage App**.
3. Go to **Settings → Secrets**.
4. Add your API keys:

```toml
GEMINI_API_KEY="your_gemini_api_key"
GROQ_API_KEY="your_groq_api_key"
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## 📄 Excel Reports

The application generates downloadable Excel reports containing:

- Summary
- BA Questions
- Test Scenarios
- Positive Test Cases
- Negative Test Cases
- Boundary Test Cases
- Risks

---


## 🎯 Future Enhancements

- Requirement Quality Analyzer
- Requirement Classification
- Duplicate Requirement Detection
- AI-powered API Test Case Generation
- PDF Report Export
- Unique Test Case IDs across reports
- Support for additional LLM providers
- AI Chat Assistant for QA Engineers

---

## 👩‍💻 Author

**Priyadarshini Murali**

QA Engineer | AI in Testing | Playwright Automation | Python

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub!
