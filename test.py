import requests
import os
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    },
    json={
        "model": "openai/gpt-oss-120b",
        "messages": [
            {
                "role": "user",
                "content": "Say hello."
            }
        ]
    }
)

print(response.status_code)
print(response.json())