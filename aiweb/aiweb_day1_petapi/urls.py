from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PetViewset

#in views only one url is required
router = DefaultRouter()
router.register('pets', views.PetViewset, basename='pet')  # basename is imp when using viewsets

urlpatterns = [
    # path('pets/', views.Pets.as_view()),
    # path('pets/<int:pk>/', views.PetDetail.as_view()),

    path('', include(router.urls)),

    # FUNCTION BASED VIEWS
    #  path('pets/', views.get_all_pets, name='get_all_pets'),
    #  path('pets/<int:pk>/', views.petDetailView)
]