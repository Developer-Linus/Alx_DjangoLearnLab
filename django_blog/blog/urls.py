from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    # Custom views for registration and profile
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    
    #views for Post CRUD operations
    path('post/', views.PostList.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    
    # Comments views
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete-comment'),
    
    #URLs for tagging and searching
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts-by-tag'),
    path("search/", views.SearchResultsView.as_view(), name="search-results"),
]