from tools.openrouter_client import ask_llm
import json

class LeadExtractAgent:

    def extract(self, text):

        prompt = f"""
You are an elite SDR researcher.

Extract ONLY information explicitly found or strongly inferred.

Return valid JSON:

{{
    "company_name":"",
    "founder_name":"",
    "founder_title":"",
    "website":"",
    "email":"",
    "phone":"",
    "whatsapp":"",
    "linkedin":"",
    "twitter":"",
    "instagram":"",
    "industry":"",
    "content_activity":"",
    "clipping_score":0,
    "outreach_angle":""
}}

If information is unavailable, return "".

Website text:

{text[:4000]}
"""

        response = ask_llm(prompt)

        print()
        print("RAW LLM RESPONSE:")
        print(response)
        print()

        try:
            return json.loads(response)
        except Exception as e:
            print("JSON ERROR:", e)
            return {}