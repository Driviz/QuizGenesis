from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView, AdminRetrieveUpdateAPIView

urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/<int:pk>/', AdminRetrieveUpdateAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('user/', UserRetrieveUpdateAPIView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
