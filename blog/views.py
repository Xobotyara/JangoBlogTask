from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostListView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.all()



""" def index(request):
    p = 'Hello world!'
    return render(request, 'index.html', context={'p':p,}) """