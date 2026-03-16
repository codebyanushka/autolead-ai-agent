from browser_use import Agent
from browser_use.llm.ollama.chat import ChatOllama

task = """
Open https://duckduckgo.com.

Search for 'makeup studios in Delhi'.

Open the first business website.

Look for any contact email address on the page.

Report the email if found.
"""

agent = Agent(
    task=task,
    llm=ChatOllama(model="llama3")
)

agent.run_sync()