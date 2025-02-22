from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def home_view(request):
    return HttpResponse('Welcome to library app.')
def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            messages.error(request, 'Error during registration. Please check your input.')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {'form': form})


# Function to check if the user is an admin
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Function to check if the user is a librarian
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# Function to check if the user is a member
def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Custom Forbidden Response
def forbidden_view(request):
    return HttpResponseForbidden("You do not have permission to access this page.")

# ✅ Admin View (Only Admins Can Access)
@user_passes_test(is_admin, login_url='/forbidden/')  # Redirect if unauthorized
def admin_view(request):
    return render(request, 'admin_dashboard.html')

# ✅ Librarian View (Only Librarians Can Access)
@user_passes_test(is_librarian, login_url='/forbidden/')
def librarian_view(request):
    return render(request, 'librarian_dashboard.html')

# ✅ Member View (Only Members Can Access)
@user_passes_test(is_member, login_url='/forbidden/')
def member_view(request):
    return render(request, 'member_dashboard.html')


