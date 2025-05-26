# views.py
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .chains import generate_pet_advice
from django.shortcuts import render

class PetAdviceAPIView(APIView):  # normal (non-expert)
    def post(self, request):
        user_input = request.data.get("question")
        if not user_input:
            return Response({"error": "Missing 'question' in request"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "tinyllama",
                    "prompt": user_input,
                    "stream": False
                },
                timeout=60
            )
            data = response.json()
            return Response({"answer": data.get("response", "No response from model.")}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PetExpertAPIView(APIView):  # expert via chains.py
    def post(self, request):
        user_input = request.data.get("question")
        if not user_input:
            return Response({"error": "Missing 'question' in request"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            answer = generate_pet_advice(user_input)
            return Response({"answer": answer}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def pet_advisor_ui(request):
    return render(request, "pet_advisor.html")
