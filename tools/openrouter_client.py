import requests
import os

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
            ]
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
