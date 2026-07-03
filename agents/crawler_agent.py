from urllib.parse import urlparse
from agents.browser_agent import BrowserAgent

# Pages we actively want (used to discover contact/social info)
GOOD_PATHS = ["", "/about", "/about-us", "/contact", "/contact-us", "/get-in-touch", "/team"]

# Known-noise paths — never crawl these even if something upstream
# tries to queue them
BAD_PATH_KEYWORDS = [
    "/blog", "/careers", "/jobs", "/privacy", "/terms", "/tos", "/legal",
    "/press", "/news", "/wp-content", "/category/", "/tag/", "/author/",
    "/login", "/signup", "/cart", "/checkout"
]

MAX_PAGES_PER_DOMAIN = 5


class CrawlerAgent:

    def crawl(self, url):
        browser = BrowserAgent()

        parsed = urlparse(url)

        # CRITICAL FIX: always crawl from the domain root, never from
        # whatever specific page (e.g. a blog post) Search happened to find.
        # This is what was causing napoleoncat.com/blog/.../contact.
        root = f"{parsed.scheme}://{parsed.netloc}"

        pages = []
        seen_urls = set()

        queue = [root + path for path in GOOD_PATHS]

        for page_url in queue:
            if len(pages) >= MAX_PAGES_PER_DOMAIN:
                break

            if page_url in seen_urls:
                continue
            seen_urls.add(page_url)

            if any(bad in page_url.lower() for bad in BAD_PATH_KEYWORDS):
                continue

            try:
                result = browser.visit(page_url)

                if not result or not result.get("text"):
                    continue

                if "couldn't find that page" in result["text"].lower():
                    continue

                if "404" in result.get("title", "").lower():
                    continue

                if len(result["text"]) < 300:
                    continue

                page_type = self._classify_page(page_url, result.get("title", ""))

                pages.append({
                    "url": page_url,
                    "title": result.get("title", ""),
                    "text": result["text"],
                    "page_type": page_type,
                })

            except Exception as e:
                print("CRAWL FAILED:", page_url, e)
                continue

        print("\n=== CRAWLED ===")
        for page in pages:
            print(page["url"], "->", page["page_type"])

        return pages

    def _classify_page(self, url, title):
        u = url.lower().rstrip("/")
        t = title.lower()

        if u.split("/")[-1] in ("about", "about-us") or "about" in t:
            return "about"
        if any(k in u for k in ["/contact", "/get-in-touch"]) or "contact" in t:
            return "contact"
        if u.count("/") <= 2:  # e.g. "https://site.com"
            return "home"
        return "other"