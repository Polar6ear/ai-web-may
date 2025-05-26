from django.urls import path
from .views import ai_advice_page, PetAdvisorView

urlpatterns = [
    path('ask-ai/', ai_advice_page, name='ask_ai'),
    path('api/ai/pet-advice/', PetAdvisorView.as_view(), name='pet_advice_api'),
]
