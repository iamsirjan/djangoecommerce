from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ManyToManyField
from django.db.models.fields.reverse_related import ManyToManyRel
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


class answer(models.Model):
    answer = models.TextField(unique=True)
    status = models.BooleanField()


class quiz(models.Model):
    answers = models.ManyToManyField(answer)
    question = models.TextField()


class result(models.Model):
    user = models.ManyToManyField(user)
    obtainmarks = models.IntegerField()
