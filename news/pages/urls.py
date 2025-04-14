from django.urls import path
from . views import HomePageView, send_test_email
urlpatterns = [
    path('send-email/', send_test_email, name='send_email'),
    path('', HomePageView.as_view(), name='home'),
]