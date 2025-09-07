# 🚀 Setup & Usage Guide – Excel Mock Interviewer

This guide explains step-by-step how to set up and run the project.  
No prior AI knowledge is required — just basic Python skills.

---

## 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/excel-mock-interviewer.git
cd excel-mock-interviewer
2️⃣ Setup Virtual Environment
It’s best to run in a virtual environment.

For Windows:
bash
Copy code
python -m venv venv
venv\Scripts\activate
For Mac/Linux:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
Dependencies include:

streamlit → Web UI

groq → LLM API

langgraph → Agent orchestration

pandas → Transcript handling

4️⃣ Setup API Key
You need a Groq API key.

Create a file named .env in the project root.

Add your key:

ini
Copy code
GROQ_API_KEY=your_api_key_here
5️⃣ Run the App
bash
Copy code
streamlit run app.py
This will open the app in your default browser (usually at http://localhost:8501).

6️⃣ Using the App
Enter your name.

Select a difficulty level (Beginner / Intermediate / Expert).

Answer Excel-related formula questions (or skip).

At the end:

See your total score.

Get personalized feedback.

Download your transcript (CSV/JSON).

7️⃣ Example Transcript Output
json
Copy code
[
  {
    "question": "Write a formula to calculate the average of column B.",
    "answer": "=AVERAGE(B:B)",
    "score": 1,
    "feedback": "Correct! You used the AVERAGE formula properly.",
    "solution": "=AVERAGE(B:B)"
  }
]
