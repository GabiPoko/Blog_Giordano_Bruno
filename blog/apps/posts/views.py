from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.


# vista basada en clases

class PostListView (ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

class PostDetailView (DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all()



