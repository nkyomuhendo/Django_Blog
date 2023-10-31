from django.shortcuts import render
from .models import Post


posts = [
    {
        'author': 'NicholasCK',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 29, 2023'
    },
    {
        'author':'Johnie Cage',
        'title':'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 30, 2023'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})