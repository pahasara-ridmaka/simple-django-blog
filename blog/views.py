from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    model = Post

    context_object_name = "all_posts_list"

    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post

    template_name = 'post_detail_view.html'
