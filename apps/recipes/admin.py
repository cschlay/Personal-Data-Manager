# MIT License
# Copyright (c) 2018 C. H. Lay

from django.contrib import admin

from apps.recipes.models import Meal, Recipe, Ingredient

admin.site.register(Meal)
admin.site.register(Recipe)
admin.site.register(Ingredient)
