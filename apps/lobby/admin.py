from django.contrib import admin

# Register your models here.
from apps.lobby.models import TimeAllocation

admin.site.register(TimeAllocation)