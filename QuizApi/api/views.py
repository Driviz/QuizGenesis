from django.shortcuts import render
from rest_framework import viewsets
from .models import QuizCategories, Quiz, Options, Questions, QuizSubCategories, User
from .serializers import QuizCategoriesSerializer, QuizSubCategoriesSerializer, QuestionsSerializer, OptionsSerializer, QuizSerializer, UserSerializer

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuizCategoriesView(viewsets.ModelViewSet):
    queryset = QuizCategories.objects.all()
    serializer_class = QuizCategoriesSerializer

class QuizSubCategoriesView(viewsets.ModelViewSet):
    queryset = QuizSubCategories.objects.all()
    serializer_class = QuizSubCategoriesSerializer

class QuestionsView(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class OptionsView(viewsets.ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer

class QuizView(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
