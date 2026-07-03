from agents.browser_agent import BrowserAgent

browser = BrowserAgent()

page = browser.visit(
    "https://www.founders.ai"
)

print(page["title"])
print()
print(page["text"][:1000])