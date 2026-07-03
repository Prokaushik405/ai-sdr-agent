from scrapegraphai.graphs import SmartScraperGraph
import os


class ScrapeGraphAgent:

    def extract(self, text):

        graph = SmartScraperGraph(

            prompt="""
You are an elite SEO researcher.

Extract the MAIN COMPANY OR CREATOR represented by this page.

Extract:

company_name
founder_name
founder_role
company_website

email
phone_number
whatsapp_number

linkedin
instagram
youtube
twitter

niche
company_description

suitable_for_clipping_agency

IMPORTANT:

Only include REAL social links:

linkedin:
must contain linkedin.com

instagram:
must contain instagram.com

youtube:
must contain youtube.com

twitter:
must contain twitter.com or x.com

Rules:
- If this page lists MULTIPLE companies/creators/podcasts (a directory, "Top 10" list, database), 
  return {"page_type": "directory", "entities": [{"name": "...", "url": "..."}]} instead of the normal schema.
- Otherwise return page_type: "single_entity" plus the fields below.
- Only extract a field if you can point to exact text supporting it. If not present, return null — 
  NEVER guess or infer a value from an unrelated page (e.g. a blog post title is not a social profile).
- A social link is only valid if it is an actual URL on that platform's domain 
  (instagram.com/..., linkedin.com/company/... or /in/..., youtube.com/..., twitter.com/... or x.com/...).
  A blog post whose slug happens to contain the word "instagram" is NOT an Instagram link

Return only valid JSON.
""",

            source=text,

            config={
                "llm": {
                    "model": "openai/gpt-oss-120b",
                    "api_key": os.getenv("OPENROUTER_API_KEY"),
                    "base_url": "https://openrouter.ai/api/v1",
                    "max_tokens": 2000
                }
            }
        )

        return graph.run()