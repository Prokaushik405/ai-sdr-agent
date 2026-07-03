from tools.openrouter_client import ask_llm


class ExtractAgent:

    def extract(self, text):

        prompt = f"""
You are an elite SDR researcher.

Analyze this website text.

Extract:

1. Company name
2. What the company does
3. Industry/Niche
4. Whether they are a good client for a clipping agency
5. A lead score from 1-10
6. A short reason

Return ONLY valid JSON.

Website text:

{text[:3000]}
"""

        return ask_llm(prompt)