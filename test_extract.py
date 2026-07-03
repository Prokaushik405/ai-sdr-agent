from agents.browser_agent import BrowserAgent
from agents.extract_agent import ExtractAgent

browser = BrowserAgent()
extractor = ExtractAgent()

page = browser.visit(
    "https://www.founders.ai"
)

result = extractor.extract(
    page["text"]
)

print(result)