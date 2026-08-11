from google import genai
from google.genai import types
from config import API_KEY


client = genai.Client(api_key=API_KEY)
MODEL = "gemini-3.1-flash-lite"

def chat(prompt: str, max_tokens=1024) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.5,
            top_p=0.95,
            max_output_tokens=max_tokens,
        )
    )

    return response.text

if __name__ == "__main__":
    print(chat("Hello there, how are you?"))