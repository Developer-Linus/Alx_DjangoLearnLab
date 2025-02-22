from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Function to check if the user is a Librarian
def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# View for Librarians
@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, 'librarian_dashboard.html', {'role': 'Librarian'})
