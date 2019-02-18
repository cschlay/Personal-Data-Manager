from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    """
    A table for tasks.
    The description should be written briefly, thus we limit it to 200 characters.
    For due dates we use format YYYY-MM-DD HH:MM.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField()
