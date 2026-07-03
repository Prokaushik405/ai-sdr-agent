from tools.openrouter_client import ask_llm
import json


class DiscoveryAgent:

    def discover(self, strategy):

        prompt = f"""
You are an elite outbound sales researcher.

Generate 50 highly specific search queries.

Strategy:

{json.dumps(strategy)}

Your goal is to discover high-value businesses and people
that show signs of growth, expansion, spending,
audience building, or market activity.

Prioritize:

- founders
- CEOs
- startups
- SaaS companies
- agencies
- ecommerce brands
- AI companies
- fintech companies
- healthcare companies
- coaches
- consultants
- creators
- podcasters
- newsletter operators
- personal brands
- media companies
- education businesses
- communities
- real estate brands

Look for signals such as:

- funding
- launches
- growth
- podcasts
- newsletters
- communities
- partnerships
- audience building
- paid ads
- expansion
- media presence

Avoid:

- news sites
- blogs
- magazines
- wikipedia
- documentation
- research pages
- job boards

Generate searches similar to:

"AI startup founder"
"SaaS CEO podcast"
"ecommerce brand founder"
"creator economy company"
"newsletter business"
"real estate founder"
"startup with funding"
"fintech company founder"
"agency owner"
"healthcare startup"
"personal brand entrepreneur"
"B2B SaaS company"
"community business"
"education company founder"

Return ONLY JSON:

[
    {{
        "query": "",
        "reason": "",
        "priority": "high"
    }}
]
"""

        try:
            result = ask_llm(prompt)
            return json.loads(result)

        except:
            return []