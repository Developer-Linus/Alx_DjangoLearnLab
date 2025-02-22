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
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied

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



def is_admin(user):
    if not hasattr(user, 'userprofile'):
        raise PermissionDenied("User profile does not exist.")
    if user.userprofile.role != 'Admin':
        raise PermissionDenied("You do not have admin privileges.")
    return True

def is_librarian(user):
    if not hasattr(user, 'userprofile'):
        raise PermissionDenied("User profile does not exist.")
    if user.userprofile.role != 'Librarian':
        raise PermissionDenied("You do not have librarian privileges.")
    return True

def is_member(user):
    if not hasattr(user, 'userprofile'):
        raise PermissionDenied("User profile does not exist.")
    if user.userprofile.role != 'Member':
        raise PermissionDenied("You do not have member privileges.")
    return True

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

