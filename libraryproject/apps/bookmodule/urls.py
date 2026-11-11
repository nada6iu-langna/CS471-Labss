from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books.index'),
    path('index2/<int:val1>/', views.index2),
    path('list_books/', views.list_books, name='books.list_books'),
    path('<int:bookId>/', views.viewbook, name='books.view_one_book'),
    path('aboutus/', views.aboutus, name='books.aboutus'),
    path('html5/links/', views.links, name='books.links'),
    # Lab 5 - Task 2
path('html5/text/formatting/', views.formatting, name='books.formatting'),
# Lab 5 - Task 3
path('html5/listing/', views.listing, name='books.listing'),
path('html5/tables/', views.tables, name='books.tables'),
path('search/', views.search, name='books.search'),
]