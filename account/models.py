from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *
# Create your models here.


class user(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=14)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
