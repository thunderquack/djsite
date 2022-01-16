from datetime import datetime
import os
from django.http import HttpRequest
from django.shortcuts import render

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
        }
    )
