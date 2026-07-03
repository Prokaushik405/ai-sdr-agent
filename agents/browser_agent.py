from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


class BrowserAgent:

    def visit(self, url):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            page = browser.new_page()

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=30000
            )

            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(3000)

            html = page.content()

            print()
            print("URL:", url)
            print("HTML SIZE:", len(html))
            print()

            browser.close() 

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        text = soup.get_text(
            separator=" ",
            strip=True
        )
        import re

        socials = re.findall(
            r'https?://(?:www\.)?(?:linkedin|instagram|twitter|x|youtube)[^\s"\']+',
            html,
            re.I
        )

        text += "\nSOCIAL_LINKS:\n"
        text += "\n".join(socials)
        print()
        print("TEXT SIZE:", len(text))
        print()
        print(text[:1000])
        print()
        return {
            "title": soup.title.string if soup.title else "",
            "text": text
        }