from rest_framework import serializers
from .models import QuizCategories, Quiz, Options, Questions, QuizSubCategories, Results

class QuizCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizCategories
        fields = ("id","title")

class QuizSubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizSubCategories
        fields = ("id","title")

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ("id","option","isAnswer", "questions")

class QuestionsSerializer(serializers.ModelSerializer):
    options = OptionsSerializer(many=True, read_only=True)
    class Meta:
        model = Questions
        fields = ("id","question","quizsubcategory","quiz", "options")

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ("id","title","time","scheduleDate","quizCategory", "questions")

class ResultsSerializer(serializers.ModelSerializer):
    # questions = QuestionsSerializer(many=True, read_only=True)
    class Meta:
        model = Results
        fields = ('id','userid','quizid','questionid','optionid', 'questions')



        