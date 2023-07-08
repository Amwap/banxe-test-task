from django.contrib.auth import login
from django.shortcuts import redirect, render
from apps.auth_app.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with the URL name of your login page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})