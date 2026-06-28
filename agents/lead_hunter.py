from tools.openrouter_client import ask_llm


def find_leads():

    prompt = """
Find 5 AI startup founders that could benefit from
a clipping agency.

Return ONLY JSON.

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

    return ask_llm(prompt)
