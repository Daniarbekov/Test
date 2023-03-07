from django.views.generic import TemplateView
from django.shortcuts import render


def index(request):
    context = {} 
    return render(request, 'index.html', context)


def page(request, page):
    context = {'page': page} 
    print(page)
    return render(request, 'index.html', context)
