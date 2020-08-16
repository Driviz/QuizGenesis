from django.contrib import admin
from .models import QuizCategories, Quiz, Options, Questions, QuizSubCategories, User
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(QuizCategories)
admin.site.register(QuizSubCategories)
admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(Options)

class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # model = CustomUser
    list_display = ('email', 'is_active', 'is_teacher')
    list_filter = ('email', 'is_active', 'is_teacher')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_teacher')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_teacher')}
        ),
    )
    search_fields = ('email','username')
    ordering = ('email','username')


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)