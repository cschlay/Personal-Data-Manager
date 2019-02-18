from django.contrib.auth.models import User
from django.db import models


class TimeAllocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    retire_date = models.DateField()
