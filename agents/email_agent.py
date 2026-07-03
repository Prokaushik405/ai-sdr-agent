import re


class EmailAgent:

    def extract(self, text):

        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )

        blacklist = [
            ".png",
            ".jpg",
            ".jpeg",
            ".svg",
            ".webp"
        ]

        clean = []

        for email in emails:

            bad = False

            for ext in blacklist:
                if ext in email:
                    bad = True

            if not bad:
                clean.append(email)

        return list(set(clean))