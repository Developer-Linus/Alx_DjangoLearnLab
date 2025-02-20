from django.urls import path
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('books/details/', list_books, name='book-details'),
    path('library/books/', LibraryDetailView.as_view(), name='library-books'),
]