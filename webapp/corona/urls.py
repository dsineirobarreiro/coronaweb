from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = "corona"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('event/', views.EventView.as_view(), name='event'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]