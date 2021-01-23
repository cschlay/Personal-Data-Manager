"""pdatamana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from apps import library, recipes
from pdatamana import settings

urlpatterns = [
    # Administration
    path('admin/', admin.site.urls),
    # Root addresses
    path('', include('django.contrib.auth.urls')),
    path('', include('apps.dashboard.urls')),
    # Budget App
    path('budget/', include('apps.budget.urls')),
    # Library App
    path('library/', include('apps.library.urls')),
    path('library/', library.views.index, name='library'),
    # Terminal App
    path('cli/', include('apps.cli.urls')),
    # Recipe App
    path('recipes/', include('apps.recipes.urls')),
    path('recipes/', recipes.views.index, name='recipes'),
    # Task App
    path('tasks/', include('apps.tasks.urls'))
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
