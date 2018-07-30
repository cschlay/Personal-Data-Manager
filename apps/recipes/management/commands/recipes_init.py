# MIT License
# Copyright (c) 2018 C. H. Lay
from django.core.management import BaseCommand

from apps.recipes.models import Meal
from pdatamana.db_settings import meals


class Command(BaseCommand):
    def handle(self, *args, **options):
        for meal in meals:
            Meal(name=meal).save()
