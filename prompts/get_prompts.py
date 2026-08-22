from pathlib import Path

BASE_DIR = Path(__file__).parent

PROMPTS = {
    file.stem: file.read_text(encoding="utf-8")
    for file in BASE_DIR.glob("*.txt")
}

browser_planner = PROMPTS.get("browser_planner", "")
