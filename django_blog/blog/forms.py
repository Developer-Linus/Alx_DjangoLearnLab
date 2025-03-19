from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile, Post, Comment

#Import for tags in forms
from taggit.models import Tag

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Form for updating user's username and email
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs = {'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['email']
        
#Form for updating user's profile picture and bio
class UpdateProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':5}))
    
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']
# Create a post form
class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas.",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Python, Django, Web development'})
    )

    class Meta:
        model = Post  # Specify the model associated with the form
        fields = ['title', 'content', 'tags']  # Include 'tags' explicitly
        
        # Add widgets to enhance styling in templates
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here...'}),
        }

    def save(self, commit=True):
        post = super().save(commit=False)

        if commit:
            post.save()

        # Handling tags manually
        tag_list = [tag.strip() for tag in self.cleaned_data['tags'].split(',') if tag.strip()]
        post.tags.set(*tag_list)  # Correctly assign tags using set()
        
        return post

#Create a comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'}),
        }
