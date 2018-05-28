from django.urls import path

from . import views

app_name = 'budget'
urlpatterns = [
    #path('', views.budget, name='budget'),
    #path('new-account/', views.new_account, name='new_account')
    path('submit/', views.submit, name='submit'),
]