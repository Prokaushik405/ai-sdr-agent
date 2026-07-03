from tools.openrouter_client import ask_llm
import json


class CEOAgent:

    def __init__(self):
        self.name = "CEO Agent"

    def think(self, mission):

        prompt = f"""
You are the CEO of an elite AI SDR agency.

MISSION:
{mission}

Your job is NOT to find companies.

Your job is to design a prospecting strategy.
Find people and companies that are actively new, growing and are from rich countries like, United States of America, Germany, Europe, France, Spain, Italy, Canada, Brazil, like tier 1 and tier 2 countries.

Your job is to design a prospecting strategy to identify
high-value businesses and individuals that are:

- actively growing
- spending money
- expanding operations
- building audiences
- launching products
- increasing market presence
- highly reachable
- likely to purchase external services

Target:

- founders
- CEOs
- startups
- SaaS companies
- agencies
- ecommerce brands
- creators
- coaches
- consultants
- personal brands
- podcasters
- newsletter operators
- educators
- communities
- media companies
- real estate brands
- fintech companies
- AI companies
- healthcare businesses
- B2B companies
- local businesses
- enterprise companies

DO NOT search for:
- news articles
- blogs
- media publications
- documentation
- research papers
- company announcements

DO NOT target:

- job listings
- hiring signals
- recruitment posts
- companies looking for employees
- freelancers
- agencies selling editing services

Rules:
- diversify countries
- diversify industries
- diversify founder types
- prioritize companies producing content
- prioritize founder-led brands
- prioritize businesses with podcasts
- prioritize businesses growing on social media
- avoid generic search terms

Return ONLY valid JSON:

{{
    "target_markets": [],
    "target_personas": [],
    "content_channels": [],
    "buying_signals": [],
    "search_topics": []
}}
"""

        try:
            result = ask_llm(prompt)
            return json.loads(result)

        except:
            return {
                "target_markets": [],
                "target_personas": [],
                "content_channels": [],
                "buying_signals": [],
                "search_topics": []
            }