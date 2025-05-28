from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.shortcuts import render

from dotenv import load_dotenv
import os

# 1. Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")  # ✅ FIXED this line

# 2. LangChain imports
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

# 3. Frontend render function
def pet_ui(request):
    return render(request, "pet_name_generator.html")


# 4. API View for pet name generation
class PetNameGenerator(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # ✅ FIXED: correct key 'pet_info'
        pet_info = request.data.get("pet_info", "")  # this should match frontend input name

        # ✅ FIXED: variable name must match
        template = PromptTemplate.from_template("Suggest 5 cute pet names for: {pet_info}")

        # LLM initialization
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

        # Chain prompt -> LLM
        chain = template | llm

        # Invoke the chain with pet_info
        names = chain.invoke({"pet_info": pet_info})

        # Return as API response
        return Response({"names": names.content})
