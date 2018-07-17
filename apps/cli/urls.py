from django.urls import path

from . import views

app_name = 'cli'
urlpatterns = [
    path('cli/', views.cli, name='cli'),


]