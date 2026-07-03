from ddgs import DDGS


def search(query, limit=5):

    results = []

    with DDGS() as ddgs:

        for r in ddgs.text(query, max_results=limit):

            results.append(
                {
                    "title": r["title"],
                    "url": r["href"]
                }
            )

    return results