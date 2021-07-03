from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import Post


def Home(request):
	return render(request, 'home.html')


def Posts(request):
	posts = Post.objects.all()
	return render(request, 'posts.html', {'posts': posts})


def Post_detail(request, slug):
	post =get_object_or_404(Post, slug=slug)
	return render(request, 'post_detail.html', {'post': post})