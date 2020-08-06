from django.db import models

# Create your models here.


# Quiz Related Models such as Categories, SubCategories, Questions, Quiz and Option can be found below
class QuizCategories(models.Model):
    title = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.title

class Quiz(models.Model):
    title = models.CharField(max_length=255, null=False)
    time = models.PositiveIntegerField(default="0")
    scheduleDate = models.DateTimeField(auto_now=True)
    quizCategory = models.ForeignKey(QuizCategories, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class SubCategories(models.Model):
    title = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.title

class Questions(models.Model):
    question = models.CharField(max_length=255, null=False)
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE)
    def __str__(self):
        return self.question

class Options(models.Model):
    option = models.CharField(max_length=255, null=False)
    isAnswer = models.BooleanField(default=False)
    questions = models.ForeignKey(Questions, related_name='options', on_delete=models.CASCADE)
    def __str__(self):
        return self.option