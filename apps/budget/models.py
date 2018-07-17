from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    value = models.CharField(max_length=50)


class Revenue(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=50, null=True)


class Spending(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=50, null=True)
