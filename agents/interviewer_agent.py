# agents/interviewer_agent.py
from utils.llm_client import ask_llm
from utils.dataset_generator import example_dataset_by_seed
import pandas as pd

class InterviewerAgent:
    """
    Generates concise, formula/explanation-only Excel questions.
    Uses history to adapt difficulty (1=Beginner,2=Intermediate,3=Advanced).
    """

    def __init__(self, candidate_name: str, level: str = "Beginner"):
        self.candidate_name = candidate_name
        self.level = level
        self.history = []
        self._difficulty_map = {"Beginner": 1, "Intermediate": 2, "Advanced": 3}
        self.difficulty = self._difficulty_map.get(level, 1)

    def _history_text(self):
        if not self.history:
            return ""
        lines = []
        for i, item in enumerate(self.history, start=1):
            q = item.get("question", "")
            a = item.get("answer", "")
            s = item.get("score", "")
            lines.append(f"Q{i}: {q}\nA{i}: {a}\nScore: {s}")
        return "\n".join(lines)

    def generate_dataset(self):
        # optional dataset for certain questions (like VLOOKUP)
        df = example_dataset_by_seed(len(self.history))
        return df

    def get_question(self, previous_answer: str = None, dataset: pd.DataFrame = None) -> dict:
        # adjust difficulty by last score
        if self.history:
            last_score = self.history[-1].get("score", None)
            if isinstance(last_score, (int, float)):
                if last_score >= 8 and self.difficulty < 3:
                    self.difficulty += 1
                elif last_score <= 3 and self.difficulty > 1:
                    self.difficulty -= 1

        dataset_csv = ""
        if dataset is None:
            dataset = self.generate_dataset()
        if isinstance(dataset, pd.DataFrame):
            dataset_csv = dataset.to_csv(index=False)

        # STRICT PROMPT CONTROL
        prompt = (
            "You are an Excel interview question generator.\n"
            "IMPORTANT RULES:\n"
            "1. Only ask questions that can be answered with an Excel formula or short explanation.\n"
            "2. Do NOT ask to insert, delete, or manually add columns/rows — only formula/concept based.\n"
            "3. Keep questions clear and exam-style, e.g., SUM, AVERAGE, VLOOKUP, IF, COUNT, INDEX, MATCH, etc.\n"
            "4. Adapt difficulty based on candidate performance.\n\n"
            f"Difficulty (1=Beginner,2=Intermediate,3=Advanced): {self.difficulty}\n"
            f"Candidate level: {self.level}\n"
        )

        hist = self._history_text()
        if hist:
            prompt += f"\nPast Q&A:\n{hist}\n"

        if previous_answer:
            prompt += f"\nLast answer: {previous_answer}\n"

        if dataset_csv:
            prompt += f"\nSample dataset (CSV):\n{dataset_csv}\n"

        prompt += "\nNow output ONE Excel formula/concept question only, no extra words."

        question_text = ask_llm(prompt, temperature=0.2)
        question_text = question_text.strip().strip('"').strip()

        # store placeholder in history
        self.history.append({
            "question": question_text,
            "answer": None,
            "score": None,
            "dataset": dataset.to_dict(orient="records")
        })
        return {"question": question_text, "dataset": dataset}
