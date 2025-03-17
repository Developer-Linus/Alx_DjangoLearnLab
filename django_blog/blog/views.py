from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            #Redirects the user to login page
            redirect('login')
    else:
        form = CustomUserCreationForm()
    return(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    # The logged in user is available as request.user
    user = request.user
    context = {'user': user}
    return render(request, 'blog/profile.html', context)
