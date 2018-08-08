from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    """
    Tracking books the user wants to keep in mind.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    read = models.BooleanField(default=False)
    hasExercises = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Exercise(models.Model):
    """
    For tracking the exercise progress of a book.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.book.title + ' ' + self.number
