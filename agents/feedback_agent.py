# agents/feedback_agent.py
from utils.llm_client import ask_llm
import json

class FeedbackAgent:
    """
    Produces a final human-friendly feedback summary using the recorded Q/A.
    """

    def __init__(self):
        pass

    def generate_summary(self, candidate_name: str, answers: list, score_scale: int = 10) -> str:
        """
        answers: list of dicts {question, answer, score, feedback, solution}
        """
        short_lines = []
        for i, a in enumerate(answers, start=1):
            short_lines.append(f"Q{i}: {a['question']} | Score: {a.get('score',0)}/{score_scale}")

        joined = "\n".join(short_lines)
        prompt = (
            f"You are an expert Excel coach. Given the following interview summary for candidate {candidate_name}, "
            "produce a brief structured feedback report: overall score, 3 strengths, 3 weaknesses, and 3 concrete next steps.\n\n"
            f"Interview summary:\n{joined}\n\nOutput should be concise and human readable."
        )
        resp = ask_llm(prompt, temperature=0.2, max_tokens=400)
        return resp.strip()
