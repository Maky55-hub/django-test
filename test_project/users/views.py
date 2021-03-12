from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} is created')
            return redirect('Blog-Home')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/registration.html', {'form': form})
