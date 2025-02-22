from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Function to check if the user is an Admin
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# View for Admins
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html', {'role': 'Admin'})
