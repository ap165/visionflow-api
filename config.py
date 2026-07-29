import os

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


