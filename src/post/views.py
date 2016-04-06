from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView
from .models import Post
from .forms import QuesForm, QuestionListForm
from django.shortcuts import resolve_url, get_object_or_404
from comment.models import Comment

class PostList(ListView):
    template_name = "post/post_list.html"
    model = Post

    def dispatch(self, request, *args, **kwargs):
        self.form = QuestionListForm(request.GET)
        self.form.is_valid()
        self.qform = QuesForm(request.POST or None)
        return super(PostList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        print self.form.cleaned_data['search']
        queryset = Post.objects.filter(title__icontains=self.form.cleaned_data['search']) #title__icontains=self.form.search
        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(title__icontains=self.form.cleaned_data['search'])
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_field'])[:10]
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['qform'] = self.qform
        return context


#class PostView(DetailView):
class PostView(DetailView):
    model = Post
    template_name = 'post/post.html'
    context_object_name = 'post'

class PostDialog(CreateView):
    model = Comment
    template_name = 'post/post.html'
    context_object_name = 'comment'
    fields = ('text',)

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.post = get_object_or_404(Post.objects.all(), pk=pk)
        return super(PostDialog, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.post = self.post
        form.instance.author = self.request.user
        return super(PostDialog, self).form_valid(form)

    def get_success_url(self):
        return resolve_url("post:post_detail", pk=self.post.pk)

    def get_context_data(self, **kwargs):
        context = super(PostDialog, self).get_context_data(**kwargs)
        context['post'] = self.post
        return context


class CommentsWithAjax(DetailView):
    template_name = 'post/post_comments_ajax.html'
    model = Post
    context_object_name = 'post'


class PostCreate(CreateView):
    model = Post
    template_name = 'post/post_create.html'
    fields = ('title', 'text')
    context_object_name = 'post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('post:post_detail', pk=self.object.pk)

class PostUpdate(UpdateView):
    template_name = 'post/post_update.html'
    model = Post
    fields = ('category', 'title', 'text', 'is_published')
    context_object_name = 'post'

    def get_queryset(self):
        return super(PostUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return resolve_url('post:post_detail', pk=self.object.pk)
