from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Custom user model manager."""

    def create_user(self, username:str, email:str, password:str, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if email and username:
            email = self.normalize_email(email)
            user = self.model(email=email, username=username, **extra_fields)
        elif email and not username:
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
        elif username and not email:
            user = self.model(username=username, **extra_fields)
        else:
            raise ValueError(_("One of email or username must be set"))
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, username:str, email:str, password:str, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username, email, password, **extra_fields)
