from django.urls import path
from .views import HomePageView, CompilerPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('compile/', CompilerPageView.as_view(), name='compile')
]
