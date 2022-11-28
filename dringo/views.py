from django.http import HttpResponse
from django.shortcuts import render


def home(request, pyaudio=None):
    return HttpResponse("First Dringo Response")


def login(request):
    return render(request, 'login.html')


def new_case(request):
    return render(request, 'not_used.html')
