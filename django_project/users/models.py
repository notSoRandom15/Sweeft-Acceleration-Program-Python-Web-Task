from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255)


    # username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)


    objects = UserManager()


class Person(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return str(self.name)
    