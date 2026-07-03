import pandas as pd


class ExportAgent:

    def export(self, leads):
        leads = sorted(
    leads,
    key=lambda x: x.get("final_score",0),
    reverse=True
)
        df = pd.DataFrame(leads)

        df.to_csv(
            "leads.csv",
            index=False
        )

        df.to_excel(
            "leads.xlsx",
            index=False
        )

        df.to_json(
            "leads.json",
            orient="records",
            indent=4
        )

        print("EXPORT COMPLETE")