from django.urls import path
from .views import PetNameGenerator, pet_ui

urlpatterns = [
    path('api/pet-name-generator/', PetNameGenerator.as_view(), name='pet-name-generator'),
    path("", pet_ui),
]