from django.shortcuts import render

# Create your views here.
def index(request):
    p = 'Hello world!'
    return render(request, 'index.html', context={'p':p,})