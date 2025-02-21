from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
from .views import LibraryDetailView
from . import views

urlpatterns = [
    path('books/details/', list_books, name='book-details'),
    path('library/books/', LibraryDetailView.as_view(), name='library-books'),
    path('', views.home_view, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

]