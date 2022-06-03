from django.urls import path

from posts.views import PostView, PostDetailView

app_name = 'posts'

urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('', PostView.as_view(), name='blog')
]