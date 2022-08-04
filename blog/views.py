import imp
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = '\blog\templates\index.html'

class PostDetail(DetailView):
    model = Post
