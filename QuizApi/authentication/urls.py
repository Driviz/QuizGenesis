from django.urls import path, include

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('users', RegistrationAPIView.as_view()),
    path('users/login', LoginAPIView.as_view()),
    path('user', UserRetrieveUpdateAPIView.as_view()),
]
