from datetime import datetime
import os
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app.forms import BlogPostForm

from app.models import Post

TEMPLATES_DIR = '../templates'


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    form = BlogPostForm()

    return render(
        request,
        os.path.join(TEMPLATES_DIR, 'index.html'),
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'blogposts': Post.objects.all,
            'form': form,
        }
    )


def create_post(request):
    """Creates post"""
    assert isinstance(request, HttpRequest)
    """
    p = Post()
    p.post = 'asdadadad'
    p.date = datetime.now()
    p.header = 'headhead'
    p.save()
    """
    return HttpResponse('')
