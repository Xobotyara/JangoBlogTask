from django.views import generic
from .models import Post, Blogger

# Create your views here.
class PostsListView(generic.ListView):
    model = Post
    template_name = 'blog/posts.html' 
    context_object_name = 'posts'


    def get_queryset(self):
            return Post.objects.all()


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html' 


class BloggersListView(generic.ListView):
    model = Blogger
    template_name = 'blog/bloggers.html'

    def get_queryset(self):
        return Blogger.objects.all()