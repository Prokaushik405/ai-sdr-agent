class TrendAgent:

    def analyze(self, lead):

        score = 0

        content = str(lead)

        keywords = [
            "funding",
            "series a",
            "series b",
            "raised",
            "launch",
            "hiring",
            "growth",
            "creator",
            "youtube",
            "podcast",
            "marketing",
            "newsletter"
        ]

        found = []

        for k in keywords:
            if k.lower() in content.lower():
                score += 10
                found.append(k)

        return {
            "trend_score": min(score,100),
            "trend_signals": found
        }