from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    """View for url home"""
    return render(request, 'pages/index.html')


def about_view(request, *args, **kwargs):
    """View for url about"""
    return render(request, 'pages/about.html', {})
