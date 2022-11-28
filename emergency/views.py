from django.shortcuts import render


def get_emergs(request):
    return render(request, 'emergs.html')


def new_emerg(request):
    return render(request, 'new_emerg.html')
