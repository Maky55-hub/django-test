from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # model tells django to which model the data from this form should be mapped
        model = User
        # the fields array specify in which order the elements of the form should be displayed in the template
        fields = ['username', 'email', 'password1', 'password2']