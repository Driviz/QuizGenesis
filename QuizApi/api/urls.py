from django.urls import path, include
from .views import QuizCategoriesView, SubCategoriesView, QuestionsView, OptionsView, QuizView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('QuizCategories', QuizCategoriesView)
router.register('SubCategories', SubCategoriesView)
router.register('Questions', QuestionsView)
router.register('Options', OptionsView)
router.register('Quiz', QuizView)

urlpatterns = [
    path('', include(router.urls)),
]