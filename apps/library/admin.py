from django.contrib import admin

# Register your models here.
from apps.library.models import Book, Exercise

admin.site.register(Book)
admin.site.register(Exercise)