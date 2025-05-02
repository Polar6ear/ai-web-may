from django.shortcuts import render
from .models import Pet
from .serializers import PetSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def get_all_pets(request):
    pets = Pet.objects.all()
    serializer = PetSerializers(pets, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
