from django.contrib.auth.models import User
from django.db import models


class Revenue(models.Model):
    account_id = models.IntegerField()
    amount  = models.IntegerField()
    comment = models.CharField(max_length = 50, null = True)

class Account(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    account_name = models.CharField(max_length = 20, null = True)