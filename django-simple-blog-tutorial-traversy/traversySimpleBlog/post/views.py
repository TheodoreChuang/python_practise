from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def index(request):
  """Return 10 posts"""
  posts = Post.objects.all()[:10]

  context = {
    'title': 'Latest Posts',
    'posts': posts
  }

  return render(request, 'post/index.html', context)


def details(request, id):
  """Show details of a single post"""
  post = Post.objects.get(id=id)

  context = {
    'post': post
  }

  return render(request, 'post/details.html', context)