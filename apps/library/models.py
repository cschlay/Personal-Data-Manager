from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    """
    Tracking books the user wants to keep in mind.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    edition = models.IntegerField(default=1)
    read = models.BooleanField(default=False)
    hasExercises = models.BooleanField(default=False)


class Exercises(models.Model):
    """
    For tracking the exercise progress of a book.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)
