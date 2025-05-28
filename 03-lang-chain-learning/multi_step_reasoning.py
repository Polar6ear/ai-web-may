import os
from dotenv import load_dotenv

# 1) Use the updated OpenAI import

from langchain.agents import Tool, initialize_agent, AgentType

# Load API key
load_dotenv()
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(  # ✅ Use chat model for function calling
    temperature=0.5,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo"  # ✅ Required for function calling (not text-davinci)
)

# 3) Define tool functions
def pet_suggestions(_):
    return "Pets suitable for small apartments:\n1. Cat\n2. Parrot\n3. Rabbit"

def pet_fun_fact(pet: str):
    return f"A fun fact about {pet}: They adapt very well to small spaces and love company."

def dog_name_gen(_):
    return "Here are some dog name ideas:\n- Bruno\n- Daisy"

def simple_math(expr: str):
    return str(eval(expr))

# 4) Define tools
tools = [
    Tool(
        name="PetSuggester",
        func=pet_suggestions,
        description="Suggests 3 pets suitable for small apartments"
    ),
    Tool(
        name="PetFunFact",
        func=pet_fun_fact,
        description="Gives a fun fact about a specified pet"
    ),
    Tool(
        name="DogNameGen",
        func=dog_name_gen,
        description="Generates creative dog name ideas"
    ),
    Tool(
        name="Calculator",
        func=simple_math,
        description="Solves simple math expressions"
    ),
]

# 5) Initialize the agent using OPENAI_FUNCTIONS (recommended for multi-step reasoning)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

# 6) Run multi-step prompts reliably
prompts = [
    "What are 3 pets suitable for small apartments? Then give a fun fact about one.",
    "Give me 2 name ideas for a dog and multiply 8 by 7."
]

for prompt in prompts:
    print(f"\n=== Prompt: {prompt}\n")
    result = agent.invoke({"input": prompt})
    print(result["output"])
