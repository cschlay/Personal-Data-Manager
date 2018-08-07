from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('submit/', views.submit, name='submit'), # /library/submit
    path('book/<int:book_id>/', views.book, name='book'), # /library/book/<book_id>
]