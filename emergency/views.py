from django.shortcuts import render, redirect

from emergency.models import Emergency
from hospital.models import Hospital
from role.models import Role


def get_emergs(request):
    if request.user.is_authenticated:
        if Role.objects.filter(employee=request.user.id).first().is_car:
            obj = Emergency.objects.all()
        else:
            obj = Emergency.objects.filter(hospital=Hospital.objects.filter(
                id=Role.objects.filter(employee=request.user.id).first().hospital.id).first())
        return render(request, 'emergs.html', {"emeges": obj})
    else:
        return redirect('/einloggen')


def remove_emerg(request, id):
    if request.user.is_authenticated:
        Emergency.objects.filter(case_id=id).delete()
        return redirect('/notfalls')
    else:
        return redirect('/einloggen')

def new_emerg(request):
    if request.user.is_authenticated:
        from django.db.models import Count
        return render(request, 'new_emerg.html')
    else:
        return redirect('/einloggen')
