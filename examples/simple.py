from dotenv import load_dotenv
from browser_use import Agent
from browser_use.llm.ollama.chat import ChatOllama

load_dotenv()

agent = Agent(
    task='Find the number of stars of the following repos: browser-use, playwright, stagehand, react, nextjs',
    llm=ChatOllama(model="llama3")
)

agent.run_sync()