from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    """View for url home"""
    return render(request, 'home.html')


def about_view(request, *args, **kwargs):
    """View for url about"""
    return render(request, 'about.html', {})


def contacts_view(request, *args, **kwargs):
    """View for url contacts"""
    return render(request, 'contacts.html', {})
