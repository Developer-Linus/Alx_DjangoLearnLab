from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

# Function to check if the user is an Admin
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Custom Forbidden Response
def forbidden_view(request):
    return HttpResponseForbidden("You do not have permission to access this page.")

# Admin View (Only Admins Can Access)
@user_passes_test(is_admin, login_url='/forbidden/')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
