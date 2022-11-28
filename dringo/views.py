from django.http import HttpResponse
from django.shortcuts import render


def home(request, pyaudio=None):
    return HttpResponse("First Dringo Response")


def login(request):
    a =[]
    return render(request, 'login.html')
