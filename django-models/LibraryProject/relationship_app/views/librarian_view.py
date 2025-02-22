from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

# Function to check if the user is a Librarian
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# Librarian View (Only Librarians Can Access)
@user_passes_test(is_librarian, login_url='/forbidden/')
def librarian_dashboard(request):
    return render(request, 'librarian_dashboard.html')
