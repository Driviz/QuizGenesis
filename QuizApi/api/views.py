from django.shortcuts import render
from rest_framework import viewsets
from .models import QuizCategories, Quiz, Options, Questions, SubCategories
from .serializers import QuizCategoriesSerializer, SubCategoriesSerializer, QuestionsSerializer, OptionsSerializer, QuizSerializer

# Create your views here.
class QuizCategoriesView(viewsets.ModelViewSet):
    queryset = QuizCategories.objects.all()
    serializer_class = QuizCategoriesSerializer

class SubCategoriesView(viewsets.ModelViewSet):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer

class QuestionsView(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class OptionsView(viewsets.ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer

class QuizView(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
