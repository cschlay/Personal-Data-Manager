from django.contrib.auth.models import User
from django.db import models


class Revenue(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    comment = models.CharField(max_length=50, null=True)


class Spending(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    comment = models.CharField(max_length=50, null=True)