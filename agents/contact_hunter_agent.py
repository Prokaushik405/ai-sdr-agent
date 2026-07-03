from duckduckgo_search import DDGS
import re


class ContactHunterAgent:

    def hunt(self, lead):

        company = lead.get("company_name", "")
        website = lead.get("company_website", "")

        searches = [
            f'"{company}" email',
            f'"{company}" contact',
            f'"{company}" support email',
            f'"{company}" founder',
            f'"{company}" linkedin',
            f'site:{website.replace("https://","").replace("http://","")} contact'
        ]

        emails = set()
        phones = set()
        founder = None

        email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
        phone_pattern = r'\+?\d[\d\s().-]{7,}\d'

        with DDGS() as ddgs:

            for q in searches:

                try:
                    for r in ddgs.text(q, max_results=5):

                        text = (
                            r.get("title","")
                            + " "
                            + r.get("body","")
                        )

                        emails.update(
                            re.findall(email_pattern, text)
                        )

                        phones.update(
                            re.findall(phone_pattern, text)
                        )

                        if not founder:
                            if "founder" in text.lower():
                                founder = text

                except:
                    pass

        if emails:
            lead["emails"] = list(emails)

        if phones:
            lead["phone_number"] = list(phones)[0]

        if founder and lead.get("founder_name") == "NA":
            lead["founder_name"] = founder[:100]

        return lead