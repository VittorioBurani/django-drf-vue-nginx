from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    [field.name for field in CustomUser._meta.get_fields()]

admin.site.register(CustomUser, CustomUserAdmin)
