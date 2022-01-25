from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


# Profile manager
class ProfileManager(BaseUserManager):

    def _create_user(self, email, password, **extra_data):
        """
        Create and save a Profile with the given email and password.
        """
        if not email:
            raise ValueError("No valid email provided.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_data)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_data):
        extra_data.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_data)

    def create_superuser(self, email, password, **extra_data):
        extra_data.setdefault("is_staff", True)
        extra_data.setdefault("is_superuser", True)

        if not extra_data.get("is_staff"):
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if not extra_data.get("is_superuser"):
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_data)


# Profile user
class Profile(AbstractUser):
    username = models.CharField(max_length=8, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=128, unique=True)

    objects = ProfileManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'
