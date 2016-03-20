from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post

class PostList(ListView):
    template_name = "blog/post_list.html"
    model = Post
    
def show_post(request, post):
    return render(request, 'post.html', {"post": post})
    
# Create your views here.
