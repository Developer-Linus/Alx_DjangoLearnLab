from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from taggit.models import Tag

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Comment

from .forms import CustomUserCreationForm, UpdateUserForm, UpdateProfileForm, PostForm, CommentForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #Redirects the user to login page
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    # The logged in user is available as request.user
    user = request.user
    context = {'user': user}
    return render(request, 'blog/profile.html', context)
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully.')
            return redirect('profile')
        else:
            # If the form is invalid, re-render the edit profile page with errors
            return render(request, 'blog/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        user_form=UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'blog/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

# View logic to display all blog posts
class PostList(ListView):
    #specify the model for list view
    model = Post
    template_name = 'blog/post_list.html'  # Template file
    context_object_name = 'object_list'  # Context variable in template

#View to show individual post
class PostDetailView(DetailView):
    #specify the model to use
    model = Post
    template_name = 'blog/post_detail.html'  # Template file
    context_object_name = 'post'
    
    # Include the context for comments in the post by overriding get_context_data method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the CommentForm to the template
        context['comment_form'] = CommentForm()
        # Pass all comments for the post to the template
        context['comments'] = self.object.comments.all() #Add comments to the context.
        return context
    
#View to create a post
class PostCreate(LoginRequiredMixin, CreateView):
    #specify the model to use
    model = Post
    form_class = PostForm  # Uses the form we created earlier
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set logged-in user as author
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})  # Redirect to the new post’s detail page
    
#View for editing posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    #specify the model to use
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can edit
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})  # Redirect to the updated post
    
    def get_initial(self):
        """Pre-fill the form with existing tags as a comma-separated string."""
        initial = super().get_initial()
        initial['tags'] = ", ".join(tag.name for tag in self.object.tags.all())
        return initial
    
    
# View to delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    #specify the model you want to use
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can delete

# View to create a comment
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_detail.html'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk'] #Adds post id
        form.instance.author = self.request.user # Adds the author
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, id=self.kwargs['pk'])  # Pass the post to the template
        return context
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})
# Updating comment
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    
    def get_queryset(self):
        #Ensure only the comment author can edit the post
        return Comment.objects.filter(author=self.request.user)
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.id})

# View for deleting comment
class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_queryset(self):
        # Ensure only the comment author can delete their own comment
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only the comment author can delete

# View for search functionality in the database
class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)).distinct() #Distinct make sure that a post is unique and no duplicates
        return Post.objects.none() #Return empty if no query
    
# View to display all posts associated with a specific tag
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags=tag)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs.get('tag_slug'))
        return context

    