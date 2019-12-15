from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    path('', RedirectView.as_view(url='bloggers')),
    path('posts/', PostsListView.as_view(), name='posts_list_url'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail_url'),
    path('bloggers/', BloggersListView.as_view(), name='bloggers_list_url'),
    
    
]
