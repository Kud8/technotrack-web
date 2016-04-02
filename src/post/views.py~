from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Post

class PostList(ListView):
    template_name = "blog/post_list.html"
    model = Post
    
class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
    
def show_post(request, post_id=0):
    return render(request, 'post.html', {"post_id": post_id})
    
# Create your views here.
