from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
from .views import LibraryDetailView
from .views import login_view, logout_view, register_view, home_view

urlpatterns = [
    path('books/details/', list_books, name='book-details'),
    path('library/books/', LibraryDetailView.as_view(), name='library-books'),
    path('', home_view, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]