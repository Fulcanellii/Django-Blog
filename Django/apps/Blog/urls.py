from django.urls import path

from .views import *

urlpatterns = [
    path('', PostsListView.as_view(), name='blog-home'),
    path('post/new', PostCreateView.as_view(), name='post-new'),
    path('post/detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
]
