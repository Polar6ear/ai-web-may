from django.shortcuts import render
from .models import Pet
from .serializers import PetSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.

# Viewsets = views + serializers + routers are used















"""
_________________
# GENERICS
___________________

from rest_framework import mixins, generics # generic ==> handel kr dega sb import convert krna serialize krna status vagera baaki update ka kaam krega < == mixins

class Pets(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializers

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializers
    lookup_field = 'pk'  # based on what we want to check

"""




# _________________
# MIXINS
# _________________


# class Pets(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Pet.objects.all()
#     serializer_class = PetSerializers
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class PetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,  generics.GenericAPIView):
#     queryset = Pet.objects.all()
#     serializer_class = PetSerializers
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk)
#
#


# ________________________
#  CLASS BASED VIEWS
# ___________________________
# class Pets(APIView):
#     def get(self, request):
#         pets = Pet.objects.all()
#         serializer = PetSerializers(pets, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = PetSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class PetDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Pet.objects.get(pk=pk)
#         except Pet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         pet = self.get_object(pk)
#         serializer = PetSerializers(pet)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         pet = self.get_object(pk)
#         serializer = PetSerializers(pet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         pet = self.get_object(pk)
#         pet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ____________________________
#  FUN BASED VIEWS
# ______________________________
# @api_view(['GET', 'POST'])
# def get_all_pets(request):
#     if request.method == 'GET':
#         pets = Pet.objects.all()
#         serializer = PetSerializers(pets, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = PetSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         print(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def petDetailView(request, pk):
#     try:
#         pet = Pet.objects.get(pk=pk)
#     except Pet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = PetSerializers(pet)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = PetSerializers(pet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         pet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
