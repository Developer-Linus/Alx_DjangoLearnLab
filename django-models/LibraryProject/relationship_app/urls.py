from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
from .views import LibraryDetailView
from .views import RegisterView

urlpatterns = [
    path('books/details/', list_books, name='book-details'),
    path('library/books/', LibraryDetailView.as_view(), name='library-books'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", RegisterView.as_view(), name="register"),
]