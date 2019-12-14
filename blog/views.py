from django.shortcuts import render
from django.views import generic
from .models import Post, Blogger

# Create your views here.
class BloggersListView(generic.ListView):
    model = Blogger

    def get_queryset(self):
        return Blogger.objects.all()
    

class PostsListView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.all()
