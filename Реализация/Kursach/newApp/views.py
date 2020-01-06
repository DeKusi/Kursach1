from django.shortcuts import render


def indexprob(request):
    return render(request, 'newApp/homePage.html')
