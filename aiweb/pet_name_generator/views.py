from rest_framework.views import APIView
from rest_framework.response import Response
from langchain.agents import Tool, initialize_agent, AgentType
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class PetNameGeneratorAPIView(APIView):
    def post(self, request):
        pet_info = request.data.get("pet_info", "")

        def name_gen(info):
            return f"Creative names for a {info}:\n1. Bolt\n2. Luna\n3. Teddy\n4. Mochi\n5. Simba"

        tools = [Tool(name="NameGen", func=name_gen, description="Generates pet names")]

        llm = OpenAI(temperature=0.5, openai_api_key=os.getenv("OPENAI_API_KEY"))

        agent = initialize_agent(
            tools,
            llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )

        output = agent.run(f"Suggest pet names for: {pet_info}")
        return Response({"names": output})
