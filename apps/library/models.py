from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    edition = models.IntegerField()
    read = models.BooleanField()