from django.contrib import admin
from .models import QuizCategories, Quiz, Options, Questions, QuizSubCategories

# Register your models here.
admin.site.register(QuizCategories)
admin.site.register(QuizSubCategories)
admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(Options)