from tools.search_tool import search

class SearchAgent:

    def search(self, query):

        print()
        print("SEARCHING:", query)
        print()

        try:

            results = search(query)

            filtered = []

            bad = [
    "wikipedia",
    "grokipedia",
    "reddit",
    "quora",
    "crunchbase",
    "youtube",
    "twitter.com",
    "x.com",
    "linkedin.com",
    "instagram.com",
    "facebook.com",
    "youtube.com",
    "/login",
"/signin",
"/signup",
"/register",
"/account",
"/auth",
"play.google.com",
"apps.apple.com",
"chrome.google.com",
"stackoverflow",
"medium.com",
"open.spotify.com"
"upwork.com",
"simplyhired.com",
"starterstory.com"
]

            for r in results:

                if any(
                    x in r["url"].lower()
                    for x in bad
                ):
                    print(
                        "SKIPPED:",
                        r["url"]
                    )
                    continue

                filtered.append(r)

            print(
                "SEARCH RESULTS:",
                len(filtered)
            )

            return filtered

        except Exception as e:

            print(
                "SEARCH FAILED:",
                query
            )

            print(e)

            return []