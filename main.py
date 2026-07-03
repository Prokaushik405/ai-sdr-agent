from agents.search_agent import SearchAgent
from agents.pipeline_agent import PipelineAgent
from agents.export_agent import ExportAgent
from agents.discovery_agent import DiscoveryAgent
from agents.signal_agent import SignalAgent
from agents.trend_agent import TrendAgent
from agents.prospect_agent import ProspectAgent
from agents.qualification_agent import QualificationAgent
from agents.ceo_agent import CEOAgent
from agents.memory_agent import MemoryAgent
from agents.reachability_agent import ReachabilityAgent
from agents.discovery_agent import DiscoveryAgent
from agents.score_agent import ScoreAgent

ceo = CEOAgent()
memory = MemoryAgent()
reach = ReachabilityAgent()
search = SearchAgent()
pipeline = PipelineAgent()
exporter = ExportAgent()
discover = DiscoveryAgent()
signal = SignalAgent()
trend = TrendAgent()
prospect = ProspectAgent()
qualifier = QualificationAgent()
discovery = DiscoveryAgent()
scorer = ScoreAgent()

all_leads = []
mission = """
Find companies that would buy
short-form content clipping services.
"""
print("CEO DONE")
strategy = ceo.think(mission)

print()
print("CEO STRATEGY")
print(strategy)
print()
MAX_LEADS = 10
print("DISCOVERY START")
plans = discovery.discover(strategy)
plans = plans[:5]
queries = []
stats = {
    "queries":0,
    "domains":0,
    "leads":0,
     "hot":0,
    "warm":0,
    "cold":0
}
print("DISCOVERY RESULT:")
print(plans)

for p in plans:
    q = p.get("query")

    if q:
        queries.append(q)

for q in queries:
    if stats["leads"] >= MAX_LEADS:
        print("MAX LEADS REACHED")
        break

    print()
    print("=" * 70)
    print("SEARCHING:", q)
    print("=" * 70)
    print()


    results = search.search(q)
    if results:
        stats["queries"] += 1


    # limit results for now
    seen_domains = set()
    for r in results[:3]:
        from urllib.parse import urlparse

        domain = urlparse(
        r["url"]
        ).netloc.lower()

        domain = domain.replace(
    "www.",
    ""
        )

        if domain in seen_domains:
            print("SKIPPING DUP:", domain)
            continue
        if memory.exists_domain(domain):
            print("SKIPPED MEMORY:", domain)
            continue


        try:
            print()
            print("PROCESSING:", r["url"])
            print()
            lead = pipeline.process(
                r["url"]
            )
            memory.save_domain(domain)
            stats["domains"] += 1

            seen_domains.add(domain)
            print()
            print("PIPELINE OUTPUT")
            print(lead)
            print()
            lead = reach.check(lead)
            print()
            print("REACHABILITY")
            print(lead)
            print()

            if not lead["reachable"]:
                continue
            if memory.exists(lead):
                continue
            signals = signal.score(lead)

            trends = trend.analyze(lead)

            lead = prospect.qualify(
                lead,
                signals,
                trends
            )

            if not lead:
                continue
            if lead.get("is_directory"):
                print("DIRECTORY FOUND — queuing", len(lead["entities"]), "entities")
                for ent in lead["entities"]:
                    target_url = ent.get("external_url") or ent.get("url_on_directory")
                    if target_url:
                        queries.append(target_url)  # or however you feed new URLs back into search/crawl
                continue
            qualification = qualifier.qualify(lead)
            lead["buying_score"] = qualification["buying_score"]
            lead["buying_signals"] = qualification["buying_signals"]

            lead = scorer.score(lead)
            if lead["priority"] == "HOT":
                stats["hot"] += 1

            elif lead["priority"] == "WARM":
                stats["warm"] += 1

            else:
                stats["cold"] += 1
            print()
            print("QUALIFICATION")
            print(qualification)
            print()
            all_leads.append(lead)
            stats["leads"] += 1
            exporter.export([lead])   
            memory.save(lead)

            
            print()
            print("="*70)
            print("CEO REPORT")
            print("="*70)

            print("Queries searched:", stats["queries"])
            print("Domains processed:", stats["domains"])
            print("Qualified:", stats["leads"])
            print("HOT:", stats["hot"])
            print("WARM:", stats["warm"])
            print("COLD:", stats["cold"])
            

            print()
            print("=" * 70)
            print("LEAD FOUND")
            print("=" * 70)
            print(lead)
            print()

        except Exception as e:

            print()
            print(
                "FAILED:",
                r["url"],
                e
            )
            print()


print()
print("=" * 70)
print("TOTAL LEADS:", len(all_leads))
print("=" * 70)
print()


exporter.export(all_leads)

print()
print("EXPORT COMPLETE")
print("leads.csv")
print("leads.xlsx")
print("leads.json")
print()