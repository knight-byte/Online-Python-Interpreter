from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib import messages
from .models import BegPost, AdvPost
from .forms import (
    UserRegisterform,
    UserUpdateform,
    ProfileUpdateform,
)


def HomePageView(response):
    return render(response, 'home.html')


#def CompilerPageView(response):
#    return render(response, 'compiler.html')


def LearnPageView(response):
    # content = {
    #     'Post': Post.objects.all()
    # }
    return render(response, 'learn.html')


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
    # return render(request, 'Signup.html', {'form': form})


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

# Beginner Post View


class BeginnerPostView(ListView):
    model = BegPost
    template_name = 'BeginnerPost.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


# @login_required
class BeginnerDetailView(LoginRequiredMixin, DetailView):
    model = BegPost
    template_name = 'beg-post-Detail.html'


class BeginnerDeleteView(LoginRequiredMixin,  UserPassesTestMixin, DeleteView):
    model = BegPost
    template_name = 'beg-post-delete.html'
    success_url = '/beginner'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BeginnerCreateView(LoginRequiredMixin, CreateView):
    model = BegPost
    fields = ['title', 'solution']
    template_name = 'beg-post-create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BeginnerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BegPost
    fields = ['title', 'solution']
    template_name = 'beg-post-create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Advance Post Vews
class AdvancePostView(ListView):
    model = AdvPost
    template_name = 'AdvancePost.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


# @login_required
class AdvanceDetailView(LoginRequiredMixin, DetailView):
    model = AdvPost
    template_name = 'post-Detail.html'


class AdvanceDeleteView(LoginRequiredMixin,  UserPassesTestMixin, DeleteView):
    model = AdvPost
    template_name = 'post-delete.html'
    success_url = '/advance'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AdvanceCreateView(LoginRequiredMixin, CreateView):
    model = AdvPost
    fields = ['title', 'solution']
    template_name = 'post-create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdvanceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AdvPost
    fields = ['title', 'solution']
    template_name = 'post-create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
