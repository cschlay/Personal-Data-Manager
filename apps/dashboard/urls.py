from django.urls import path

from . import views

urlpatterns = [
    # Root
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings')
]
