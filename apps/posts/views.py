from django.shortcuts import render

from .models import Post

def index(request):
    return render(request, 'posts/index.html', {'posts': Post.objects.order_by("-created_at")})

def add(request):
    Post.objects.create(post=request.POST['post'])
    return render(request, 'posts/post.html', {'posts': Post.objects.order_by("-created_at")})