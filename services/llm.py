from openai import OpenAI
from config import NVIDIA_API_KEY
import json


client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = NVIDIA_API_KEY
)


def chat(prompt):
  completion = client.chat.completions.create(
    model="meta/llama-3.2-3b-instruct",
    messages=[{"role":"user","content":prompt}],
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024,
    stream=False
  )

  return (completion.choices[0].message.content)


if __name__ == "__main__":
  print(print(chat("Hello there, how are you?")))