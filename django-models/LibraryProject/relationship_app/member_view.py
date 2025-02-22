from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Function to check if the user is a Member
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# View for Members
@user_passes_test(is_member)
def member_dashboard(request):
    return render(request, 'member_dashboard.html', {'role': 'Member'})
