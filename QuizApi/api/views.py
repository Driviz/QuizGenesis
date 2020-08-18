from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from .models import QuizCategories, Quiz, Options, Questions, QuizSubCategories, Results
from .serializers import QuizCategoriesSerializer, QuizSubCategoriesSerializer, QuestionsSerializer, OptionsSerializer, QuizSerializer, ResultsSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.
class QuizCategoriesView(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = QuizCategories.objects.all()
    serializer_class = QuizCategoriesSerializer

class QuizSubCategoriesView(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = QuizSubCategories.objects.all()
    serializer_class = QuizSubCategoriesSerializer

class QuestionsView(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class OptionsView(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer

class QuizView(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class ResultsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
