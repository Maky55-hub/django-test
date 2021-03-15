from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            # send an activation email
            email_subject = 'testing'
            email_body = 'new email'
            email_from = 'noreply@django-test.com'
            email_to = form.cleaned_data['email']

            email_message = EmailMessage(
                email_subject,
                email_body,
                email_from,
                [email_to]
            )
            #email_message.send(fail_silently=False)

            form.save()
            # show a success message, after a user account is created
            messages.success(request, f'Account for {username} is created')
            return redirect('Blog-Home')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/registration.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')