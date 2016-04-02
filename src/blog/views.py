from django.shortcuts import render
from django.views.generic.list import ListView
from post.views import Post

class BlogView(ListView):
    template_name = "blog/post_list.html"
    model = Post

# Create your views here.
