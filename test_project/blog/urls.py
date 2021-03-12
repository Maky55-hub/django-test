from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='Blog-About'),
    path('', views.home, name='Blog-Home'),
]