from django.urls import path
from .views import (BeginnerPostView,
                    BeginnerDetailView,
                    BeginnerCreateView,
                    BeginnerUpdateView,
                    BeginnerDeleteView,

                    AdvancePostView,
                    AdvanceDetailView,
                    AdvanceCreateView,
                    AdvanceUpdateView,
                    AdvanceDeleteView,
                    )
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    #path('compile/', views.CompilerPageView, name='compile'),
    path('learn/', views.LearnPageView, name='learn'),
    # path('login/', views.Register, name='register'),
    path('Signup/', views.Register, name='register'),
    path('profile/', views.Profile, name='profile'),
    # Beginner urls
    path('beginner/', BeginnerPostView.as_view(), name='BegPage'),
    path('beginner/<int:pk>/',
         BeginnerDetailView.as_view(), name='beg-post-detail'),
    path('beginner/new/', BeginnerCreateView.as_view(), name='BegCreate'),
    path('beginner/<int:pk>/update',
         BeginnerUpdateView.as_view(), name='beg-post-update'),
    path('beginner/<int:pk>/delete',
         BeginnerDeleteView.as_view(), name='beg-post-delete'),

    # Advance Urls
    path('advance/', AdvancePostView.as_view(), name='AdvPage'),
    path('advance/<int:pk>/',
         AdvanceDetailView.as_view(), name='adv-post-detail'),
    path('advance/new/', AdvanceCreateView.as_view(), name='AdvCreate'),
    path('advance/<int:pk>/update',
         AdvanceUpdateView.as_view(), name='adv-post-update'),
    path('advance/<int:pk>/delete',
         AdvanceDeleteView.as_view(), name='adv-post-delete'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
