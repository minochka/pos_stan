from django.urls import path

from .views import Home, Posts, Post_detail

urlpatterns = [
	path('', Home, name='home'),
	path('posts/', Posts, name='posts'),
	path('posts/<str:slug>/', Post_detail, name='post_detail')
]