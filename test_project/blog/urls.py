from django.urls import path
from . import views
from .views import (
    PostListView,
    UserPostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView)

urlpatterns = [
    path('about', views.about, name='Blog-About'),
    path('post/<int:pk>', PostDetailView.as_view(), name='Post-Detail'),
    path('post/new', PostCreateView.as_view(), name='Post-Create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='Post-Update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='Post-Delete'),
    path('post/user/<str:username>', UserPostListView.as_view(), name='User-Posts'),
    path('', PostListView.as_view(), name='Blog-Home'),
]