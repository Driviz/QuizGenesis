from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_teacher = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    objects = UserManager()
    def __str__(self):
        return self.username

# Quiz Related Models such as Categories, QuizSubCategories, Questions, Quiz and Option can be found below
class QuizCategories(models.Model):
    title = models.CharField(max_length=255, null=False)
    class Meta:
        verbose_name_plural = "QuizCategories"
    def __str__(self):
        return self.title

class Quiz(models.Model):
    title = models.CharField(max_length=255, null=False)
    time = models.PositiveIntegerField(default="0")
    scheduleDate = models.DateTimeField(default=now)
    quizCategory = models.ForeignKey(QuizCategories, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Quizes"
    def __str__(self):
        return self.title

class QuizSubCategories(models.Model):
    title = models.CharField(max_length=255, null=False)
    class Meta:
        verbose_name_plural = "QuizSubCategories"
    def __str__(self):
        return self.title

class Questions(models.Model):
    question = models.CharField(max_length=255, null=False)
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    quizsubcategory = models.ForeignKey(QuizSubCategories, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Questions"
    def __str__(self):
        return self.question

class Options(models.Model):
    option = models.CharField(max_length=255, null=False)
    isAnswer = models.BooleanField(default=False)
    questions = models.ForeignKey(Questions, related_name='options', on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Options"
    def __str__(self):
        return self.option
    