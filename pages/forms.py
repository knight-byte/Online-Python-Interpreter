from django import forms as f
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterform(UserCreationForm):
    email = f.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
