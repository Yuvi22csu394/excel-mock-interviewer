# graph/nodes.py
# Lightweight node wrappers for the LangGraph-like orchestrator.
from agents.interviewer_agent import InterviewerAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.feedback_agent import FeedbackAgent

class InterviewerNode:
    def __init__(self, candidate_name: str, level: str):
        self.agent = InterviewerAgent(candidate_name, level)

    def get_question(self, previous_answer=None, dataset=None):
        return self.agent.get_question(previous_answer=previous_answer, dataset=dataset)

class EvaluatorNode:
    def __init__(self, score_scale: int = 10):
        self.agent = EvaluatorAgent(score_scale=score_scale)

    def evaluate(self, question, answer, dataset_csv=None):
        return self.agent.evaluate(question, answer, dataset_csv)

class FeedbackNode:
    def __init__(self):
        self.agent = FeedbackAgent()

    def summarize(self, candidate_name, answers, score_scale=10):
        return self.agent.generate_summary(candidate_name, answers, score_scale)
