from django.urls import path
from .views import AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView, AuthorDetailView, BookListView, BookCreateView, BookUpdateView, BookDeleteView, BookDetailView


urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book-detail'),
]