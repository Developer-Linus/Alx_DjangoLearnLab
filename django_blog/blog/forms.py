from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile, Post, Comment

#Import for tags in forms
from taggit.forms import TagWidget

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
from django import forms
from taggit.forms import TagWidget
from .models import Post

# Create a Post form with tagging functionality included using TagWidget
class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Specify the model associated with the form
        fields = ['title', 'content', 'tags']  # Include 'tags' explicitly

        # Add widgets to enhance styling in templates
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here...'}),
            'tags': TagWidget(),
        }

#Create a comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'}),
        }
