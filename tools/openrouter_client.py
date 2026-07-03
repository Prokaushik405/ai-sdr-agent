from dotenv import load_dotenv
import os
import requests

load_dotenv()

OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "openai/gpt-oss-120b"


def ask_llm(prompt):

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 4000
        },
        timeout=120
    )

    if response.status_code != 200:
        print("=== OPENROUTER ERROR ===")
        print("Status:", response.status_code)
        print("Body:", response.text)
        print("=========================")

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]