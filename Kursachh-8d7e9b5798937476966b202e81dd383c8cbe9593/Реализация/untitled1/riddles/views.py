from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .forms import PlaneForm
from .models import plane, fly
from django.shortcuts import get_object_or_404


def riddles(request):
    form = PlaneForm(request.POST or None)
    n = ['Лол', ' кек', ' чебурек']
    planes = plane.objects.all()
    return render(request, 'riddles/riddles.html', {'form': form,
                                                    'lol': n,
                                                    'planes': planes})


def air_detail(request, plane_id):
    # air = plane.objects.get(id__iexact=plane_id)
    air = get_object_or_404(plane, id__iexact=plane_id)
    return render(request, 'riddles/air_detail.html', {'air': air})


def fly_list(request):
    flys = fly.objects.all()
    return render(request, 'riddles/fly_list.html', context={'flys': flys})


def fly_detail(request, fly_id):
    # flyy = fly.objects.get(id__iexact=fly_id)
    flyy = get_object_or_404(fly, id__iexact=fly_id)
    return render(request, 'riddles/fly_detail.html', {'fly': flyy})
