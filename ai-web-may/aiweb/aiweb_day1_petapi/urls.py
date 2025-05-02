from django.urls import path
from . import views
urlpatterns = [
    path('pets/', views.get_all_pets, name='get_all_pets'),
]