class QualificationAgent:

    def qualify(self, lead):

        score = 0
        signals = []

        if lead.get("youtube"):
            score += 20
            signals.append("youtube")

        if lead.get("instagram"):
            score += 10
            signals.append("instagram")

        if lead.get("twitter"):
            score += 10
            signals.append("twitter")

        if lead.get("linkedin"):
            score += 10
            signals.append("linkedin")

        if lead.get("discord"):
            score += 10
            signals.append("discord")

        niche = str(
            lead.get(
                "niche",
                ""
            )
        ).lower()

        buyers = [
            "agency",
            "coach",
            "creator",
            "founder",
            "podcast",
            "saas",
            "education",
            "personal brand"
        ]

        for b in buyers:
            if b in niche:
                score += 20
                signals.append(b)

        return {
            "buying_score": score,
            "buying_signals": list(
                set(signals)
            )
        }