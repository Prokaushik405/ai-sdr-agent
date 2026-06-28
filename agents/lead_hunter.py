from tools.openrouter_client import ask_llm


def find_leads(niche):

    prompt = f"""
    Find 5 companies/founders in the niche:

    {niche}

    Return JSON:

    [
        {{
            "name":"",
            "company":"",
            "website":"",
            "reason":""
        }}
    ]
    """

    return ask_llm(prompt)
