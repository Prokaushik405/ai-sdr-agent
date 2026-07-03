class ProspectAgent:

    def qualify(self, lead, signals, trends):

        final_score = (
            signals["lead_score"] +
            trends["trend_score"]
        )

        if final_score > 120:
            final_score = 100

        if final_score >= 80:
            tier = "A"

        elif final_score >= 60:
            tier = "B"

        else:
            tier = "C"

        lead["final_score"] = final_score
        lead["tier"] = tier
        lead["trend_signals"] = trends["trend_signals"]

        return lead