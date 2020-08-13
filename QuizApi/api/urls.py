from django.urls import path, include
from .views import QuizCategoriesView, QuizSubCategoriesView, QuestionsView, OptionsView, QuizView, ResultView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('QuizCategories', QuizCategoriesView)
router.register('QuizSubCategories', QuizSubCategoriesView)
router.register('Questions', QuestionsView)
router.register('Options', OptionsView)
router.register('Quiz', QuizView)
router.register('Result',ResultView)
urlpatterns = [
    path('', include(router.urls)),
]