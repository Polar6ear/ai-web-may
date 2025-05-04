from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter
router.register('pets', )
urlpatterns = [



    """
    
    # CLASS BASED VIEWS
    
    path('pets/', views.Pets.as_view()),
    path('pets/<int:pk>/', views.PetDetail.as_view())
    
    """


    # FUNCTION BASED VIEWS
    #  path('pets/', views.get_all_pets, name='get_all_pets'),
    #  path('pets/<int:pk>/', views.petDetailView)
]