# 📊 Excel Mock Interviewer (Agentic AI with LangGraph)

This project is an **AI-powered Excel Mock Interviewer** built using **Agentic AI concepts** and **LangGraph orchestration**.  
It simulates a real-world **Excel interview** where a candidate is asked formula-based and function-based questions such as **SUM, AVERAGE, VLOOKUP, IF, PivotTables**, etc.  

The interviewer adapts dynamically to the candidate’s performance — if the candidate answers correctly, the difficulty level increases; if not, it adjusts to give slightly simpler questions. At the end of the interview, the candidate receives **personalized feedback, scoring, and the option to download a transcript** of their performance.

---

## 🔑 Problem Statement
Traditional Excel interviews are static and do not adapt to the candidate’s level of understanding.  
This project solves that problem by using **Agentic AI with LangGraph**, where multiple agents (Interviewer, Evaluator, Feedback) work together to:
1. **Ask dynamic questions** based on Excel formulas and functions.  
2. **Evaluate answers** in real-time using an LLM.  
3. **Provide feedback and solutions** at the end.  
4. **Generate a downloadable transcript** for review.  

---

## ⚙️ Frameworks & Tools Used

### 1. **LangGraph**
- Used to design an **agentic workflow** where multiple agents collaborate:
  - `InterviewerAgent` → Generates questions dynamically.  
  - `EvaluatorAgent` → Evaluates answers & assigns scores.  
  - `FeedbackAgent` → Summarizes performance and provides personalized feedback.  

### 2. **Streamlit**
- Provides a **professional, interactive interface** for candidates.  
- Features:
  - Candidate name & level selection.  
  - Submit and Skip buttons for each question.  
  - Final report with **score + feedback**.  
  - Downloadable transcript (JSON/CSV).  

### 3. **Groq API with Llama 3.1 8B Instant**
- The chosen **Large Language Model (LLM)** for:
  - Understanding candidate answers.  
  - Checking correctness against expected solutions.  
  - Generating human-like feedback.  

**Why Llama 3.1 8B Instant?**
- **Fast inference** → makes real-time evaluation smooth.  
- **Smaller model size (8B)** → suitable for interview-scale tasks without heavy infra.  
- **Trained for reasoning** → handles formula evaluation and explanations well.  

---

## 🧩 Project Architecture

excel-mock-interviewer/
│── app.py # Main Streamlit app
│── agents/
│ ├── interviewer_agent.py # Handles question generation
│ ├── evaluator_agent.py # Evaluates answers using LLM
│ └── feedback_agent.py # Generates final feedback
│── data/
│ └── questions.json # Predefined Excel question bank
│── utils/
│ ├── llm_client.py # Wrapper for Groq API (Llama 3.1 Instant)
│ └── transcript.py # Save/export transcript
│── requirements.txt # Dependencies
│── README.md
│── USAGE.md


---

## 📊 Example Workflow

1. Candidate enters **name** and selects **difficulty level** (Beginner/Intermediate/Expert).  
2. System asks a **formula-based question** (e.g., *"Write a formula to calculate the average of column B."*).  
3. Candidate submits answer → **Evaluator Agent** checks correctness.  
4. Based on score, **next question difficulty is adjusted**.  
5. After test ends → Candidate receives:
   - Final **score**.  
   - **Feedback** on performance.  
   - **Transcript download** with:
     - Question  
     - Candidate Answer  
     - Correct Solution  
     - Score (0/1)  
     - AI Feedback  

---

## 📈 Features
- 🤖 **Agentic AI-driven adaptive interviews**  
- 🎯 **Formula/function-based Excel questions**  
- ⏭️ **Submit / Skip options**  
- 📊 **Score + Personalized feedback**  
- 📥 **Downloadable transcript** (CSV/JSON)  

---

## 🚀 Future Scope
- Add **case-study style Excel tasks** (pivot tables, charts).  
- Integrate with **real Excel sheets** to auto-validate answers.  
- Extend to **other Office tools** (Word, PowerPoint).  

---

## 📸 Screenshots (to add after running)
- Candidate login screen.  
- Question with Submit/Skip.  
- Final score + feedback page.  
- Transcript download option.

- ---

## 📝 License

This project is licensed under the **MIT License**.  
You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the project, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the software.  
2. The software is provided "as is", without warranty of any kind.

---

## © Rights & Ownership

© 2025 Yuvraj Mudgil. All rights reserved.  
This project and its contents are original work developed by the author and may not be reproduced or used commercially without explicit permission.
