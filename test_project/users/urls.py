from django.urls import path
from . import views


urlpatterns = [
    path('registration', views.user_registration, name='User-Registration'),
    path('profile', views.profile, name='Profile')
]
