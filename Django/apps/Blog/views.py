from django.views.generic import ListView, CreateView, DetailView
from .models import Post

class PostsListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_posted']
    context_object_name = 'posts'
    paginate_by = 5

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
