from google import genai
from google.genai import types
from config import API_KEY


system_instruction = """
You are VisionFlow AI, an intelligent and reliable assistant.
Provide accurate, helpful, and well-structured responses. Prioritize factual correctness and clearly state any uncertainty instead of guessing.
Write naturally in clear English. Use clean Markdown with headings, lists, tables, and code blocks when they improve readability. Keep responses concise unless the user requests more detail.
Adapt your tone and level of detail to the user's request. Be creative in explanations and examples, but never at the expense of accuracy.
For coding tasks, write clean, production-quality code following best practices.
Always answer the user's intent directly. Do not include unnecessary filler, repetition, or meta commentary.
"""


client = genai.Client(api_key=API_KEY)
MODEL = "gemini-3.1-flash-lite"

def chat(prompt: str, max_tokens=1024) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
            temperature=0.5,
            top_p=0.95,
            max_output_tokens=max_tokens,
        )
    )

    return response.text




if __name__ == "__main__":
    print(chat("Hello there, how are you?"))