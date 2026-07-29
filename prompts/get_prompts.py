from pathlib import Path

PROMPTS = {
    file.stem: file.read_text(encoding="utf-8")
    for file in Path("prompts").glob("*.txt")
}

classification_prompt = PROMPTS["classification"]
conversation_action_prompt = PROMPTS["conversation"]
browser_action_prompt = PROMPTS["browser_action"]
summarizer_prompt = PROMPTS["summarizer"]