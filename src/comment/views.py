from django.shortcuts import render
from models import Comment
from django.views.generic import CreateView, UpdateView
from django.shortcuts import resolve_url

# Create your views here.

class CommentCreate(CreateView):
    model = Comment
    fields = ('text',)
    context_object_name = 'comment'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('post:post_detail', pk=self.object.pk)
