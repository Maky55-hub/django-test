from django.urls import path
from . import views

urlpatterns = [
    path('about', views.About, name='Blog-About'),
    path('', views.Home, name='Blog-Home'),
]