
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('bloggers/', views.BloggersListView.as_view(), name='bloggers_list_url'),
    path('posts/', views.PostsListView.as_view(), name='posts_list_url'),
    path('', RedirectView.as_view(url='posts')),
]
