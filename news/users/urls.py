from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignUpView
from django.views.generic import TemplateView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
