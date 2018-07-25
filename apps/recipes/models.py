from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)


class Ingredient(models.Model):
    name = models.CharField(max_length=50)


class Unit(models.Model):
    value = models.CharField(max_length=5)


class RecipeContains(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    priority = models.IntegerField()


class Procedure(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    number = models.IntegerField()
    description = models.CharField(max_length=150)