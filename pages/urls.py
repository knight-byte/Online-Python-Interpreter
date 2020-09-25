from django.urls import path
# from .views import HomePageView, CompilerPageView, LearnListView
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('compile/', views.CompilerPageView, name='compile'),
    path('learn/', views.LearnPageView, name='learn'),
    path('Signup/', views.Register, name='register'),
    path('profile/', views.Profile, name='profile'),

]
