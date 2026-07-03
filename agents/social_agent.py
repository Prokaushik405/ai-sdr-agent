import re
from urllib.parse import urlparse


class SocialAgent:

    # Every platform now requires its URL to actually be ON that platform's
    # domain. This is the fix for the NapoleonCat bug: a URL like
    # napoleoncat.com/blog/how-to-post-reels-on-instagram is on
    # napoleoncat.com, NOT instagram.com, so it will now be correctly ignored.
    PLATFORM_DOMAINS = {
        "linkedin": ["linkedin.com"],
        "twitter": ["twitter.com", "x.com"],
        "instagram": ["instagram.com"],
        "youtube": ["youtube.com", "youtu.be"],
        "discord": ["discord.gg", "discord.com"],
        "telegram": ["t.me", "telegram.me"],
        "whatsapp": ["wa.me", "chat.whatsapp.com"],
    }

    BAD_PATH_SEGMENTS = [
        "/jobs", "/search", "/feed", "/embed", "/watch?", "/playlist",
        "/hashtag", "/status", "/posts", "/reels", "/explore", "/blog"
    ]

    def extract(self, text):
        socials = {platform: [] for platform in self.PLATFORM_DOMAINS}

        urls = re.findall(r'https?://[^\s"\'<>]+', text)

        for raw_url in urls:
            url = raw_url.rstrip('/.,;)')

            try:
                domain = urlparse(url).netloc.lower().replace("www.", "")
            except Exception:
                continue

            matched_platform = None
            for platform, domains in self.PLATFORM_DOMAINS.items():
                if domain in domains:
                    matched_platform = platform
                    break

            if not matched_platform:
                continue

            if any(bad in url.lower() for bad in self.BAD_PATH_SEGMENTS):
                continue

            # extra structural checks per platform
            if matched_platform == "twitter" and "/search" in url:
                continue
            if matched_platform == "youtube" and ("/embed" in url or "/watch" in url):
                continue
            if matched_platform == "linkedin" and "/company/" not in url and "/in/" not in url:
                continue

            socials[matched_platform].append(url)

        # de-duplicate, keep first occurrence (real profile links usually
        # live in header/footer, which appears earliest in page text)
        for platform in socials:
            socials[platform] = list(dict.fromkeys(socials[platform]))[:1]

        return socials