class SignalAgent:

    def score(self, lead):

        score = 0
        reasons = []

        if lead.get("emails"):
            score += 20
            reasons.append("email")

        if lead.get("phone_numbers"):
            score += 20
            reasons.append("phone")

        if lead.get("founder_name"):
            score += 15
            reasons.append("founder")

        if lead.get("founder_linkedin"):
            score += 10
            reasons.append("linkedin")

        if lead.get("content_activity"):
            score += 15
            reasons.append("content")

        socials = lead.get("socials", {})

        for platform in socials:
            if socials[platform]:
                score += 5

        if score >= 70:
            priority = "HOT"

        elif score >= 40:
            priority = "WARM"

        else:
            priority = "COLD"

        return {
            "lead_score": score,
            "priority": priority,
            "signals": reasons
        }