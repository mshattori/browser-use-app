import sys
from langchain.chat_models import init_chat_model
from browser_use import Agent
import asyncio

class AgentError(Exception):
    """Custom exception for agent errors."""
    pass

async def main(prompt):
    agent = Agent(
        task=prompt,
        llm=init_chat_model(model='gpt-4o-mini'),
    )
    result = await agent.run()
    if result is None:
        raise AgentError('No result returned from the agent.')

    if result.has_errors():
        raise AgentError('The agent encountered errors during execution.')

    return result.final_result()

if __name__ == '__main__':
    prompt = sys.argv[1]
    output = asyncio.run(main(prompt))
    print(output)
