from logging import PlaceHolder
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Profile


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email')


class LogInForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'placeholder': 'ex: x123456'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': '********'}))
