from agents.discovery_agent import DiscoveryAgent
from agents.trend_agent import TrendAgent
from agents.signal_agent import SignalAgent
from agents.prospect_agent import ProspectAgent


class CEOAgent:

    def __init__(self):

        self.discovery = DiscoveryAgent()
        self.trend = TrendAgent()
        self.signal = SignalAgent()
        self.prospect = ProspectAgent()

    def create_searches(self, niches):

        searches = []

        for niche in niches:

            discovered = self.discovery.discover(niche)

            for item in discovered:

                trend_data = self.trend.analyze(item)

                signal_data = self.signal.score(item)

                prospect = self.prospect.qualify(
                    item,
                    signal_data,
                    trend_data
                )

                if prospect:
                    searches.append(
                        prospect["query"]
                    )

        return list(set(searches))