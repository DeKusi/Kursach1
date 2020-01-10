from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world!")

def boot (request):
    return render(request, 'boot.html', {})

def new (request):
    return render(request, 'newApp/homePage.html', {})

