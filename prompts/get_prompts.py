from pathlib import Path

PROMPTS = {
    file.stem: file.read_text(encoding="utf-8")
    for file in Path().glob("*.txt")
}

classification_prompt = PROMPTS["classification"]
planner_prompt = PROMPTS["planner"]
vision_prompt = PROMPTS["vision"]
summarizer_prompt = PROMPTS["summarizer"]