from django.contrib import admin

# Register your models here.
from apps.budget.models import Revenue, Spending, Category

admin.site.register(Revenue)
admin.site.register(Spending)
admin.site.register(Category)