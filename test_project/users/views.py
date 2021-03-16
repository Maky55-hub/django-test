from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


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
            messages.success(request, f'Account for {username} is created!')
            return redirect('Blog-Home')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/registration.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm( request.POST,
                                    request.FILES, 
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('Profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)