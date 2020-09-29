from django.urls import path
# from .views import HomePageView, CompilerPageView, LearnListView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('compile/', views.CompilerPageView, name='compile'),
    path('learn/', views.LearnPageView, name='learn'),
    # path('login/', views.Register, name='register'),
    path('Signup/', views.Register, name='register'),
    path('profile/', views.Profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
