from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from langchain_ollama import OllamaLLM

class PetAdvisorView(APIView):
    def post(self, request):
        prompt = request.data.get("query")
        llm = OllamaLLM(model="llama3")
        response = llm.invoke(prompt)
        return Response({"response": response})

def ai_advice_page(request):
    return render(request, 'aichat/ai_advice.html')

