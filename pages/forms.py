from django import forms as f
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterform(UserCreationForm):
    email = f.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateform(f.ModelForm):
    email = f.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateform(f.ModelForm):
    class Meta:
        model = Profile
        fields = ['images']
