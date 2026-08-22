from google import genai
from google.genai import types
from config import API_KEY

client = genai.Client(api_key=API_KEY)
MODEL = "gemini-3.1-flash-lite" # Or whichever multimodal model you are using

def chat(prompt: str, audio_bytes: bytes = None, mime_type: str = "audio/webm", max_tokens=1024) -> str:
    # 1. Start with the text prompt
    contents = [prompt]
    
    # 2. If audio bytes are provided, attach them as a Part
    if audio_bytes:
        audio_part = types.Part.from_bytes(
            data=audio_bytes,
            mime_type=mime_type,
        )
        contents.append(audio_part)

    # 3. Send both the text and audio to Gemini
    response = client.models.generate_content(
        model=MODEL,
        contents=contents,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.5,
            top_p=0.95,
            max_output_tokens=max_tokens,
        )
    )

    return response.text