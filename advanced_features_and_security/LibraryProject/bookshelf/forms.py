from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
from .models import Book
from django import forms

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = '__all__'

class ExampleForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label="Book Title",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the book title'})
    )
    author = forms.CharField(
        max_length=100,
        label="Author",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the author name'})
    )
    publication_year = forms.IntegerField(
        label="Publication Year",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the publication year'})
    )

    def clean_publication_year(self):
        """Custom validation for the publication_year field."""
        publication_year = self.cleaned_data.get('publication_year')
        if publication_year < 0:
            raise forms.ValidationError("Publication year cannot be negative.")
        if publication_year > 2025:  # Example: Assume 2025 is the maximum allowed year
            raise forms.ValidationError("Publication year cannot be in the future.")
        return publication_year