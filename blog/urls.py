from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView
                    )
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]