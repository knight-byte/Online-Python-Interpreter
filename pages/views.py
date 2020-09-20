from django.shortcuts import render

# from django.views.generic import TemplateView, ListView
from .models import Post


# class HomePageView(TemplateView):
#     template_name = "home.html"


# class CompilerPageView(TemplateView):
#     template_name = "compiler.html"


# class LearnListView(ListView):
#     model = Post
#     template_name = 'learn.html'


def HomePageView(response):
    return render(response, 'home.html')


def CompilerPageView(response):
    return render(response, 'compiler.html')


def LearnPageView(response):
    content = {
        'Post': Post.objects.all()
    }
    return render(response, 'learn.html', content)
