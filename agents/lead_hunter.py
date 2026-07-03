from tools.openrouter_client import ask_llm
import json


def find_leads():

    prompt = """
You are an elite SDR researcher.

Find 3 REAL AI startup founders or AI companies.

Requirements:
- Must be real.
- Must have a website.
- Must be active online.
- Must likely benefit from a clipping agency.

Return ONLY valid JSON.

Format:

[
    {
        "name":"",
        "company":"",
        "website":"",
        "email":"",
        "reason":""
    }
]
"""

    response = ask_llm(prompt)

    return response