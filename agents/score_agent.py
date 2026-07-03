class ScoreAgent:

    def score(self, lead):

        score = 0

        # contact data
        if lead.get("founder_name"):
            score += 10

        if lead.get("emails"):
            score += 20

        if lead.get("phone_number"):
            score += 15

        # socials
        if lead.get("linkedin"):
            score += 10

        if lead.get("youtube"):
            score += 10

        if lead.get("instagram"):
            score += 5

        if lead.get("twitter"):
            score += 5

        # trend signals
        score += lead.get("trend_score", 0) * 0.20

        # buying intent
        score += lead.get("buying_score", 0) * 0.40

        # existing lead score
        score += lead.get("lead_score", 0) * 0.25

        score = int(min(score, 100))

        lead["final_score"] = score

        if score >= 80:
            lead["priority"] = "HOT"

        elif score >= 60:
            lead["priority"] = "WARM"

        else:
            lead["priority"] = "COLD"

        return lead