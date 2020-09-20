from django.shortcuts import render

from .models import Post


def HomePageView(response):
    return render(response, 'home.html')


def CompilerPageView(response):
    return render(response, 'compiler.html')


def LearnPageView(response):
    content = {
        'Post': Post.objects.all()
    }
    return render(response, 'learn.html', content)
