from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

# Function to check if the user is a Member
def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Member View (Only Members Can Access)
@user_passes_test(is_member, login_url='/forbidden/')
def member_dashboard(request):
    return render(request, 'member_dashboard.html')
