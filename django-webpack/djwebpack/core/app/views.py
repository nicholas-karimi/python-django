from django.shortcuts import render
from datetime import datetime as datetime


def home(request):
    assert request
    return render(
        request, 'index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year
        }
    )