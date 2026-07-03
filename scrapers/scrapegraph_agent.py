from scrapegraphai.graphs import SmartScraperGraph
import os
graph = SmartScraperGraph(
prompt = """
You are an elite SDR and lead enrichment researcher.

Your job is to extract ALL possible outreach channels.

Find:

company_name
founder_name
founder_role
company_website

emails:
- support emails
- founder emails
- sales emails
- press emails
- public emails

phone_number:
- company phone number

whatsapp_number:
- whatsapp business number

linkedin:
- company linkedin
- founder linkedin

instagram:
- company instagram
- founder instagram

youtube:
- company youtube

twitter:
- company twitter/X

discord:
- discord invite

telegram:
- telegram channel

niche:
- exact business niche

company_description:
- one sentence summary

suitable_for_clipping_agency:
true or false

IMPORTANT:

Search priority:
1. Email
2. Phone
3. WhatsApp
4. LinkedIn
5. Instagram
6. Twitter
7. YouTube
8. Discord
9. Telegram

If email does not exist,
return social profiles.

If socials do not exist,
return founder/company information.

Never omit a valid contact method.

Return ONLY JSON.
""",

    source="https://jasper.ai",

    config={
        "llm": {
            "model": "openai/gpt-oss-120b",
            "api_key": os.getenv("OPENROUTER_API_KEY"),
            "base_url": "https://openrouter.ai/api/v1"
        }
    }
)

result = graph.run()

print(result)