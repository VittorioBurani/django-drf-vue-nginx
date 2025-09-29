from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    # Custom fields:
    email = models.EmailField(unique=True)
    password_reset_required = models.BooleanField(default=True)
    # Engine for CustomUser:
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()
