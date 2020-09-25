from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import Post
from .forms import UserRegisterform


def HomePageView(response):
    return render(response, 'home.html')


def CompilerPageView(response):
    return render(response, 'compiler.html')


def LearnPageView(response):
    content = {
        'Post': Post.objects.all()
    }
    return render(response, 'learn.html', content)


def Register(request):
    if request.method == 'POST':
        form = UserRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your Account has been Created! You Can Login')
            return redirect('login')
    else:
        form = UserRegisterform()
    return render(request, 'Signup.html', {'form': form})


@login_required
def Profile(request):
    return render(request, 'profile.html')
