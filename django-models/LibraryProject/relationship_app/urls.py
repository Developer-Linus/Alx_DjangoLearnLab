from django.urls import path
from . import views

urlpatterns = [
    path('/books/details', views.book_list, name='book-details'),
    path('/library/books', views.LibraryDetailView.as_view(), name='library-books'),
]