# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# LLM (Groq / Llama 3.1 instant)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.1-8b-instant")

# Interviewer Info
INTERVIEWER_NAME = os.getenv("INTERVIEWER_NAME", "Yuvraj")

# Interview Settings
MAX_QUESTIONS = int(os.getenv("MAX_QUESTIONS", 5))
SCORE_SCALE = int(os.getenv("SCORE_SCALE", 10))
TIME_LIMIT = int(os.getenv("TIME_LIMIT", 600))  # total seconds for interview (optional)
