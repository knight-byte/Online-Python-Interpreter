from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import Post
from .forms import UserRegisterform, UserUpdateform, ProfileUpdateform


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
    if request.method == 'POST':
        u_form = UserUpdateform(request.POST, instance=request.user)
        p_form = ProfileUpdateform(
            request.POST,
            request.FILES,
            instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Your Account has been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateform(instance=request.user)
        p_form = ProfileUpdateform(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)
