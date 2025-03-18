from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

from .forms import CustomUserCreationForm, UpdateUserForm, UpdateProfileForm, PostForm

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
    template_name = 'blog/list_post.html'  # Template file
    context_object_name = 'object_list'  # Context variable in template

#View to show individual post
class PostDetailView(DetailView):
    #specify the model to use
    model = Post
    template_name = 'blog/detail_post.html'  # Template file
    context_object_name = 'post'
    
#View to create a post
class PostCreate(LoginRequiredMixin, CreateView):
    #specify the model to use
    model = Post
    form_class = PostForm  # Uses the form we created earlier
    template_name = 'blog/create_post.html'

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
    template_name = 'blog/update_post.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can edit
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})  # Redirect to the updated post
    
    
# View to delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    #specify the model you want to use
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can delete
            
