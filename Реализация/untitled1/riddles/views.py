from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .forms import PlaneForm


def riddles(request):
    form = PlaneForm(request.POST or None)
    n = ['Лол',' кек',' чебурек']
    return render(request, 'riddles/riddles.html', {'form': form, 'lol': n})
