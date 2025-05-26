# urls.py
from django.urls import path
from .views import PetAdviceAPIView, PetExpertAPIView, pet_advisor_ui

urlpatterns = [
    path("api/ai/pet-advice/", PetAdviceAPIView.as_view(), name="pet_advice"),
    path("api/ai/pet-expert/", PetExpertAPIView.as_view(), name="pet_expert"),
    path("pet-advisor/", pet_advisor_ui, name="pet_advisor_ui"),
]
