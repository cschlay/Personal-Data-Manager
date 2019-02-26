from django.urls import path

from . import views

app_name = 'cli'
urlpatterns = [
    path('', views.cli, name='cli'),


]