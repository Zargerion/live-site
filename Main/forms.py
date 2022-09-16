from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Required to change of password.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
