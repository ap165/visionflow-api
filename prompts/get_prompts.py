from pathlib import Path

PROMPTS = {
    file.stem: file.read_text(encoding="utf-8")
    for file in Path("prompts").glob("*.txt")
}

browser_planner = PROMPTS["browser_planner"]
