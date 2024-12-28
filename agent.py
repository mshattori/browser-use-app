import sys
from langchain.chat_models import init_chat_model
from browser_use import Agent
import asyncio

async def main(prompt):
    agent = Agent(
        task=prompt,
        llm=init_chat_model(model='gpt-4o-mini'),
    )
    result = await agent.run()
    print(result)

if __name__ == '__main__':
    prompt = sys.argv[1]
    asyncio.run(main(prompt))
