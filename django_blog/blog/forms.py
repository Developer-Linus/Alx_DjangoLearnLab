from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile, Post

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
    class Meta: #Specify the Meta Class to be used
        #Specify the model to be used
        model = Post
        # Specify the methods to be used
        fields = [
            'title', 
            'content',
        ]
    

