from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
from .views import LibraryDetailView
from . import views
from .views.admin_view import admin_dashboard
from .views.librarian_view import librarian_dashboard
from .views.member_view import member_dashboard

urlpatterns = [
    path('books/details/', list_books, name='book-details'),
    path('library/books/', LibraryDetailView.as_view(), name='library-books'),
    path('', views.home_view, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),
]