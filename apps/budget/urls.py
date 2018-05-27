from django.urls import path

from . import views

app_name = 'budget'
urlpatterns = [
    #path('', views.budget, name='budget'),
    #path('new-account/', views.new_account, name='new_account')
    path('add-income/', views.add_revenue_record, name='add-income')
]