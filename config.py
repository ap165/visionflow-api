import os

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")


