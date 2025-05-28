from django.urls import path
from .views import PetNameGeneratorAPIView

urlpatterns=[
    path('api/pet-name-generator/', PetNameGeneratorAPIView.as_view()),
]