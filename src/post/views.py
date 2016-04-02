from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Post
from .forms import QuesForm, QuestionListForm

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

    #Post.objects.filter(Q(is_published=True) | Q(author=request.user))


class PostView(DetailView):
    model = Post
    template_name = 'post/post.html'
    context_object_name = 'post'

class CommentsWithAjax(DetailView):
    template_name = 'post/post_comments_ajax.html'
    model = Post
    context_object_name = 'post'


# Create your views here.
