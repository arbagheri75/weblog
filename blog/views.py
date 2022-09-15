from django.views import generic
from .models import Post
from .forms import PostModelForm
from django.urls import reverse_lazy


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_list.html'


class PostCreateView(generic.CreateView):
    form_class = PostModelForm
    template_name = 'blog/post_create.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostModelForm
    template_name = 'blog/post_create.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')