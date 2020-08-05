from django.shortcuts import render


def home(request):
    return render(request, 'opencv/home.html')


def about(request):
    return render(request, 'opencv/about.html')
