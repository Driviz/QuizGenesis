from django.urls import path, include

from .views import RegistrationAPIView

urlpatterns = [
    path('', RegistrationAPIView.as_view()),
]