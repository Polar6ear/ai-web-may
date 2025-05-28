import os
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.agents import Tool, initialize_agent, AgentType
load_dotenv()

llm = OpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))
# Define tools
def pet_fact(input):
    return f"{input} is a wonderful companion. Always loving and loyal."

def simple_math(input):
    return str(eval(input))

tools = [
    Tool(
        name="PetFacts",
        func=pet_fact,
        description="Provides interesting pet facts"
    ),
    Tool(
        name="Calculator",
        func=simple_math,
        description="Solves simple math problems"
    )
]

# Create the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run the agent
response = agent.run("Tell me something about a parrot and also what is 25*4?")
print(response)
