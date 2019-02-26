from django.contrib.auth.models import User
from django.db import models


class ItemType(models.Model):
    name = models.CharField(max_length=50)


class Item(models.Model):
    """
    Represents a single item, preferably added those which are commonly bought.
    """
    name = models.CharField(unique=True,max_length=50)
    category = models.ForeignKey(ItemType, on_delete=models.CASCADE, blank=True)


class IncomeType(models.Model):
    """
    Income types such as Advertising revenues from service X.
    """
    name = models.CharField(max_length=50)


class Income(models.Model):
    """
    A model for incomes, everything is supposed to be uploaded.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()
    description = models.CharField(max_length=50, blank=True)
    type = models.ForeignKey(IncomeType, on_delete=models.CASCADE, blank=True)


class Spending(models.Model):
    """
    We think that every spending is spent on an item, whether a physical product or a service.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()
    description = models.CharField(max_length=50, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
