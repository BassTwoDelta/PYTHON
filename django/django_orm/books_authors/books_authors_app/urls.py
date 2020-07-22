from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.author),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('books/<num>', views.book_page),
    path('authors/<num>', views.author_page),
    path('books/<num>/add_author_to_book', views.add_author_to_book),
    path('authors/<num>/add_book_to_author', views.add_book_to_author)
]
