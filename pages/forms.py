from django import forms as f
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserRegisterform(UserCreationForm):
    # username=f.username    email = f.EmailField()
    username = f.CharField(label=_(""), max_length=50, help_text='',
                           widget=(f.TextInput(attrs={'class': 'form-control txtb', 'placeholder': 'UserName'})))
    email = f.EmailField(label=_(""), max_length=50, help_text='',
                         widget=(f.TextInput(attrs={'class': 'form-control txtb', 'placeholder': 'Email'})))
    password1 = f.CharField(label=_(""),
                            widget=(f.PasswordInput(
                                    attrs={'class': 'form-control txtb', 'placeholder': 'Password'})),
                            help_text=(""))
    password2 = f.CharField(label=_(""), widget=f.PasswordInput(attrs={'class': 'form-control txtb', 'placeholder': 'Password Confirmation'}),
                            help_text=_(''))

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
