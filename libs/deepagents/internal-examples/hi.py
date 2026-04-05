from langchain_core.messages import HumanMessage

from deepagents import create_deep_agent

print("Done, imported deepagents without any problem hehe :)")

agent = create_deep_agent(
    model="openrouter:qwen/qwen3.6-plus:free",
    system_prompt="You're an agent, just say hi :)",
    tools=[],
    middleware=[],
)

# result = agent.invoke({"messages": [HumanMessage("explain machine learning to me in nice way")]})
