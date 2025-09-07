
# 📊 Excel Mock Interviewer - Usage Guide

This document explains how to set up, run, and use the **Excel Mock Interviewer** project built with **Agentic AI** using **LangGraph** and **LLM models**.

---

## 1. Prerequisites

Before running the project, make sure you have:

1. **Python 3.10+** installed.
2. **Git** installed to clone the repository.
3. A **Groq API key** for accessing the LLM.
4. Basic knowledge of running commands in a terminal.
5. ---

## 2. Clone the Repository

Open your terminal or command prompt and run:

bash
git clone https://github.com/<your-username>/excel-mock-interviewer.git
cd excel-mock-interviewer
Replace <your-username> with your GitHub username.

3. Set Up a Virtual Environment

Create a Python virtual environment to manage dependencies:

python -m venv venv


Activate the virtual environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

4. Install Dependencies

Install the required Python packages using requirements.txt:

pip install -r requirements.txt


Dependencies include:

streamlit → for building the web interface.

groq → for accessing the LLM (Groq API wrapper).

python-dotenv → for managing API keys securely.

pandas → for working with datasets in questions.

regex → for formula validation.

5. Configure API Keys

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=llama-3.1-8b-instant
INTERVIEWER_NAME=YourName


Replace your_groq_api_key_here with your actual Groq API key.

You can customize the interviewer’s name with INTERVIEWER_NAME.

6. Run the Project

Run the Streamlit web app:

streamlit run app.py


Your default browser will open with the interview interface.

Enter your name and select a skill level: Beginner, Intermediate, or Advanced.

7. How to Use the Interview Interface

Start Interview
Enter your name and select your skill level. Click Start Interview.

Answer Questions

Questions will appear one by one.

You can type your formula or explanation in the answer box.

Click Submit Answer to record your response.

If you want to skip, click Skip Question.

Dynamic Question Flow

The agent adjusts the difficulty of the next question based on your previous answer.

Beginner → Intermediate → Advanced progression is adaptive.

Feedback & Transcript

After completing all questions, you will receive a detailed report.

The report includes:

Candidate answers

Correct solutions

Scores

Feedback

You can download your transcript in JSON format.

8. File Structure Overview
excel-mock-interviewer/
├── app.py                  # Main Streamlit app
├── config.py               # API keys & settings
├── agents/                 # Agentic AI components
│   ├── interviewer_agent.py
│   ├── evaluator_agent.py
│   └── feedback_agent.py
├── utils/                  # Helpers like API wrappers
│   └── groq_client.py
└── data/
    ├── transcripts/        # Stores interview transcripts
    └── candidates.json     # Optional candidate profiles

9. Notes & Tips

Ensure internet connection for LLM API calls.

Make sure your Groq API key is valid.

Do not hardcode the candidate name; the interface asks for it each time.

You can modify the question bank and scoring logic by updating the agents folder.

10. Troubleshooting

Streamlit Errors → Make sure you installed all dependencies and activated the virtual environment.

API Authentication Errors → Check .env for correct API key.

JSON Transcript Issues → Ensure data/transcripts folder exists.
