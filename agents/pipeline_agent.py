from agents.browser_agent import BrowserAgent
from agents.email_agent import EmailAgent
from agents.social_agent import SocialAgent
from agents.lead_extract_agent import LeadExtractAgent
from agents.crawler_agent import CrawlerAgent
from agents.scrapegraph_agent import ScrapeGraphAgent
from agents.score_agent import ScoreAgent
from agents.contact_hunter_agent import ContactHunterAgent


class PipelineAgent:

    def __init__(self):
        self.browser = BrowserAgent()
        self.email = EmailAgent()
        self.social = SocialAgent()
        self.extractor = LeadExtractAgent()
        self.crawler = CrawlerAgent()
        self.scrape = ScrapeGraphAgent()
        self.score = ScoreAgent()
        self.hunter = ContactHunterAgent()

    def process(self, url):

        pages = self.crawler.crawl(url)

        if not pages:
            return None

        print("=== PAGES TO SCRAPEGRAPH ===")
        for p in pages:
            print(p["url"], p["page_type"], len(p["text"]))

        # FIX: pages are kept clearly separated with URL + page_type labels,
        # and each page is capped individually — not concatenated into one
        # undifferentiated blob. This is what let blog text get treated as
        # "the company" and let unrelated links bleed together.
        combined = ""
        for page in pages:
            combined += f"\n\n=== PAGE ({page['page_type']}): {page['url']} ===\n"
            combined += page["text"][:3000]

        print("=== COMBINED TEXT SIZE ===", len(combined))

        result = self.scrape.extract(combined)

        print("=== SCRAPEGRAPH RAW ===")
        print(type(result))
        print(result)

        if isinstance(result, dict) and "content" in result:
            result = result["content"]

        if not isinstance(result, dict):
            result = {}

        # Directory pages (Feedspot, Heepsy, "Top 50 X" lists) return a list
        # of entities instead of one company. Hand this back to the caller
        # so each entity can be re-queued as its own prospect, instead of
        # forcing the directory owner to become the "lead".
        if result.get("page_type") == "directory":
            return {
                "is_directory": True,
                "source_url": url,
                "entities": result.get("entities", []),
            }

        lead = {
            "company_name": result.get("company_name", "NA"),
            "founder_name": result.get("founder_name", "NA"),
            "founder_role": result.get("founder_role", "NA"),
            "company_website": url,
            "emails": result.get("emails", []) or [],
            "phone_number": result.get("phone_number", "NA"),
            "whatsapp_number": result.get("whatsapp_number", "NA"),
            "linkedin": "NA",
            "instagram": "NA",
            "youtube": "NA",
            "twitter": "NA",
            "discord": "NA",
            "telegram": "NA",
            "niche": result.get("niche", "NA"),
            "company_description": result.get("company_description", ""),
            "suitable_for_clipping_agency": result.get("suitable_for_clipping_agency", False),
        }

        # FIX: run regex extraction PER PAGE then merge — not on the giant
        # blob — so a real social link on the homepage isn't diluted or
        # confused by noise text on other pages.
        merged_emails = set()
        merged_socials = {"linkedin": [], "twitter": [], "instagram": [],
                           "youtube": [], "discord": [], "telegram": [], "whatsapp": []}

        for page in pages:
            for e in self.email.extract(page["text"]):
                merged_emails.add(e)

            page_socials = self.social.extract(page["text"])
            for platform, links in page_socials.items():
                merged_socials[platform].extend(links)

        if merged_emails:
            lead["emails"] = list(merged_emails)

        for platform in ["linkedin", "twitter", "instagram", "youtube", "discord", "telegram", "whatsapp"]:
            found = list(dict.fromkeys(merged_socials[platform]))
            lead[platform] = found[0] if found else "NA"

        lead["source"] = url

        # fallback contact hunter if still nothing usable
        if (
            not lead.get("emails")
            and lead.get("phone_number", "NA") == "NA"
            and lead.get("linkedin", "NA") == "NA"
        ):
            lead = self.hunter.hunt(lead)

        lead = self.score.score(lead)

        print("=== FINAL LEAD ===")
        print(lead)

        return lead