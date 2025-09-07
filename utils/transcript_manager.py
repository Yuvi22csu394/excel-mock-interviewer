# utils/transcript_manager.py
import os
import json
from pathlib import Path

TRANSCRIPT_DIR = Path("data") / "transcripts"
TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)

def save_transcript(candidate_name: str, transcript: list) -> str:
    safe = candidate_name.replace(" ", "_")
    path = TRANSCRIPT_DIR / f"{safe}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(transcript, f, indent=2, ensure_ascii=False)
    return str(path)

def load_transcript(candidate_name: str) -> list:
    safe = candidate_name.replace(" ", "_")
    path = TRANSCRIPT_DIR / f"{safe}.json"
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
