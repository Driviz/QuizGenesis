from rest_framework import serializers
from .models import QuizCategories, Quiz, Options, Questions, SubCategories

class QuizCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizCategories
        fields = ("id","title")

class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = ("id","title")

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ("id","option","isAnswer", "questions")

class QuestionsSerializer(serializers.ModelSerializer):
    options = OptionsSerializer(many=True)
    class Meta:
        model = Questions
        fields = ("id","question","subcategory","quiz", "options")

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True)
    class Meta:
        model = Quiz
        fields = ("id","title","time","scheduleDate","quizCategory", "questions")



        