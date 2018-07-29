# MIT License
# Copyright (c) 2018 C. H. Lay
from django.core.management import BaseCommand

from apps.recipes.models import Meal


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Recipes
        meals: [] = ["breakfast", "lunch", "snack", "dinner", "supper"]

        for meal in meals:
            Meal(name=meal).save()
