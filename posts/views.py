from django.shortcuts import render
from django.views.generic import ListView, DetailView

from posts.models import PostModel


class PostView(ListView):
    queryset = PostModel.objects.order_by('-pk')
    template_name = 'blog.html'
    paginate_by = 3



class PostDetailView(DetailView):
    template_name = 'blog-details.html'
    model = PostModel
