from openai import OpenAI
from config import NVIDIA_API_KEY
import json


client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = NVIDIA_API_KEY
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string"
                    }
                },
                "required": ["query"]
            }
        }
    }
]


def chat(prompt, max_tokens=1024):
  completion = client.chat.completions.create(
    model="meta/llama-3.2-3b-instruct",
    messages=[{"role":"user","content":prompt}],
    temperature=0.3,
    top_p=0.7,
    max_tokens=max_tokens,
    stream=False,
  )
  

  return (completion.choices[0].message.content)


if __name__ == "__main__":
  print(print(chat("Hello there, how are you?")))