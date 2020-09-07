from django.urls import path
from .views import HomePageView, CompilerPageView, LearnPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('compile/', CompilerPageView.as_view(), name='compile'),
    path('learn/', LearnPageView.as_view(), name='learn'),

]
