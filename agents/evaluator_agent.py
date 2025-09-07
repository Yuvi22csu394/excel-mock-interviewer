# agents/evaluator_agent.py
from utils.llm_client import ask_llm
import json
import re

class EvaluatorAgent:
    """
    Evaluates the candidate's answer and MUST return strict JSON:
    { "score": int (0..SCORE_SCALE), "feedback": str, "solution": str }
    """

    def __init__(self, score_scale: int = 10):
        self.score_scale = score_scale

    def evaluate(self, question_text: str, answer_text: str, dataset_csv: str = None) -> dict:
        """
        Ask the LLM to evaluate and return parseable JSON.
        The prompt enforces JSON-only output.
        """
        # Build prompt forcing JSON output
        prompt = (
            "You are an Excel expert evaluator. "
            "Your output MUST be valid JSON only, with keys: score (0..{scale}), feedback (string, concise), solution (string - a correct Excel formula or clear steps). "
            "Do not output any extra text, explanation, or surrounding backticks. "
        ).format(scale=self.score_scale)

        prompt += f"\nQuestion: {question_text}\nCandidate Answer: {answer_text}\n"
        if dataset_csv:
            prompt += f"Dataset CSV:\n{dataset_csv}\n"

        prompt += (
            "\nAssess correctness, clarity, edge cases, and provide a numeric score 0-"
            f"{self.score_scale}. If the candidate answer is a formula, include the corrected formula in 'solution'."
            " Respond ONLY with JSON."
        )

        raw = ask_llm(prompt, temperature=0.0, max_tokens=300)

        # Try to extract JSON object from raw text
        json_text = self._extract_json(raw)
        if not json_text:
            # fallback: create minimal error JSON
            return {"score": 0, "feedback": "Error parsing evaluator response.", "solution": "N/A", "raw": raw}

        try:
            parsed = json.loads(json_text)
            # normalize fields
            score = parsed.get("score", 0)
            try:
                score = int(round(float(score)))
            except:
                score = 0
            feedback = parsed.get("feedback", "")
            solution = parsed.get("solution", "")
            return {"score": score, "feedback": feedback, "solution": solution, "raw": raw}
        except Exception:
            return {"score": 0, "feedback": "Error parsing evaluator response.", "solution": "N/A", "raw": raw}

    def _extract_json(self, text: str) -> str:
        """
        Extract the first JSON object from the model output.
        """
        import regex as re
        # find first { ... } balanced
        m = re.search(r"\{(?:[^{}]|(?R))*\}", text, flags=re.DOTALL)
        if m:
            return m.group(0)
        return None
