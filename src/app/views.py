from datetime import datetime
import os
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from app.models import Post

TEMPLATES_DIR = '../templates'


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        os.path.join(TEMPLATES_DIR, 'index.html'),
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'blogposts': Post.objects.all
        }
    )


def create_post(request):
    """Creates post"""
    assert isinstance(request, HttpRequest)
    return HttpResponse('')
