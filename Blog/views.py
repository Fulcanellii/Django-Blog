from django.shortcuts import render
from django.views.generic import ListView
from Blog.models import Post

class PostsListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_posted']
    context_object_name = 'posts'
    paginate_by = 5

