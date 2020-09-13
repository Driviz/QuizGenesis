from django.urls import path, include
from .views import QuizCategoriesView, QuizSubCategoriesView, QuestionsView, OptionsView, QuizView, ResultsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('QuizCategories', QuizCategoriesView)
router.register('QuizSubCategories', QuizSubCategoriesView)
router.register('Questions', QuestionsView)
router.register('Options', OptionsView)
router.register('Quiz', QuizView)
router.register('Results', ResultsView)

urlpatterns = [
    path('', include(router.urls)),
]