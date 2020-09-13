from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User
# Register your models here.
class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # model = CustomUser
    list_display = ('email', 'is_active')
    list_filter = ('email', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        # ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        # ('Important dates', {'fields': ('updated_at', 'created_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','username')
    ordering = ('email','username')


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)