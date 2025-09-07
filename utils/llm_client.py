# utils/llm_client.py
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME
import time

_client = Groq(api_key=GROQ_API_KEY)

def ask_llm(prompt: str, temperature: float = 0.2, max_tokens: int = 512):
    """
    Send a prompt to the configured LLM model and return the assistant text.
    Caller should ensure the prompt instructs the model to output in the desired format.
    """
    # Basic retry wrapper
    for attempt in range(3):
        try:
            response = _client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a focused assistant that follows instructions exactly."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            text = response.choices[0].message.content
            if isinstance(text, str):
                return text.strip()
            return str(text).strip()
        except Exception as e:
            last_exception = e
            time.sleep(0.5 + attempt * 0.5)
    raise last_exception
