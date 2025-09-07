# app.py
import streamlit as st
import pandas as pd
import time
from graph.builder import build_workflow
from utils.transcript_manager import save_transcript
from config import INTERVIEWER_NAME, MAX_QUESTIONS, SCORE_SCALE, TIME_LIMIT

st.set_page_config(page_title="Excel Mock Interview", page_icon="📊", layout="wide")
st.title("📊 Excel Mock Interviewer")
st.markdown("A dynamic, agentic Excel skills assessor.")

# session init
if "started" not in st.session_state:
    st.session_state.started = False
if "candidate_name" not in st.session_state:
    st.session_state.candidate_name = ""
if "level" not in st.session_state:
    st.session_state.level = ""
if "workflow" not in st.session_state:
    st.session_state.workflow = None
if "answers" not in st.session_state:
    st.session_state.answers = []
if "current" not in st.session_state:
    st.session_state.current = None
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# Landing
if not st.session_state.started:
    with st.form("start"):
        st.text_input("Your name", key="candidate_name")
        st.selectbox("Skill level", ["Beginner", "Intermediate", "Advanced"], key="level")
        submitted = st.form_submit_button("Start Interview")
    if submitted and st.session_state.candidate_name.strip():
        candidate = st.session_state.candidate_name.strip()
        level = st.session_state.level
        st.session_state.workflow = build_workflow(candidate, level)
        st.session_state.answers = []
        st.session_state.start_time = time.time()
        # generate first question
        qobj = st.session_state.workflow["interviewer"].get_question()
        st.session_state.current = qobj
        st.session_state.started = True
        st.rerun()
    else:
        st.info("Enter your name and select a level to begin.")

# Main interview UI
else:
    elapsed = int(time.time() - st.session_state.start_time) if st.session_state.start_time else 0
    remaining = max(0, TIME_LIMIT - elapsed)
    # Sidebar info
    with st.sidebar:
        st.markdown(f"**Candidate:** {st.session_state.candidate_name}")
        st.markdown(f"**Interviewer:** {INTERVIEWER_NAME}")
        st.markdown(f"**Progress:** {len(st.session_state.answers)}/{MAX_QUESTIONS}")
        st.markdown(f"**Elapsed:** {elapsed}s")
        st.progress(min(1.0, len(st.session_state.answers) / MAX_QUESTIONS))

    # If done
    if len(st.session_state.answers) >= MAX_QUESTIONS or remaining == 0:
        st.success("Interview complete")
        total = sum(a.get("score", 0) for a in st.session_state.answers)
        st.markdown(f"**Total Score:** {total}/{MAX_QUESTIONS * SCORE_SCALE}")
        # Finalize: summary
        summary = st.session_state.workflow["feedback"].summarize(st.session_state.candidate_name, st.session_state.answers, SCORE_SCALE)
        st.subheader("Final feedback")
        st.write(summary)
        # Save transcript and allow download
        path = save_transcript(st.session_state.candidate_name, st.session_state.answers)
        with open(path, "r", encoding="utf-8") as f:
            blob = f.read()
        st.download_button("Download transcript (JSON)", blob, file_name=f"{st.session_state.candidate_name}_transcript.json")
        # stop
        st.stop()

    # Show current question
    qobj = st.session_state.current
    st.subheader(f"Question {len(st.session_state.answers)+1}")
    st.write(qobj["question"])

    # Show dataset if present
    if qobj.get("dataset") is not None:
        df = pd.DataFrame(qobj["dataset"])
        st.markdown("Dataset (for reference):")
        st.dataframe(df)
        dataset_csv = df.to_csv(index=False)
    else:
        dataset_csv = None

    # Answer input
    answer = st.text_area("Your answer (formula/explanation):", key=f"ans_{len(st.session_state.answers)}")

    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Submit Answer"):
            eval_res = st.session_state.workflow["evaluator"].evaluate(qobj["question"], answer, dataset_csv)
            # store structured entry
            entry = {
                "question": qobj["question"],
                "answer": answer,
                "score": int(eval_res.get("score", 0)),
                "feedback": eval_res.get("feedback", ""),
                "solution": eval_res.get("solution", "")
            }
            st.session_state.answers.append(entry)
            # update interviewer history (last appended in agent)
            # Ask interviewer to produce next question using previous answer and dataset
            next_qobj = st.session_state.workflow["interviewer"].get_question(previous_answer=answer, dataset=None)
            st.session_state.current = next_qobj
            st.rerun()

    with col2:
        if st.button("Skip Question"):
            entry = {
                "question": qobj["question"],
                "answer": "<skipped>",
                "score": 0,
                "feedback": "Skipped by candidate",
                "solution": "N/A"
            }
            st.session_state.answers.append(entry)
            next_qobj = st.session_state.workflow["interviewer"].get_question(previous_answer=None, dataset=None)
            st.session_state.current = next_qobj
            st.rerun()
