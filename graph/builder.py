# graph/builder.py
from graph.nodes import InterviewerNode, EvaluatorNode, FeedbackNode
from config import SCORE_SCALE

def build_workflow(candidate_name: str, level: str):
    interviewer = InterviewerNode(candidate_name, level)
    evaluator = EvaluatorNode(score_scale=SCORE_SCALE)
    feedbacker = FeedbackNode()
    return {"interviewer": interviewer, "evaluator": evaluator, "feedback": feedbacker}
