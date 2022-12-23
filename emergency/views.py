from django.db.models import Count
from django.shortcuts import render, redirect

from emergency.models import Emergency
from hospital.models import Hospital
from role.models import Role

# Own Moduls

import operator
from django.db.models import Q
from functools import reduce


def get_emergs(request):
    if request.user.is_authenticated:
        if Role.objects.filter(employee=request.user.id).first().is_car:
            obj = Emergency.objects.all()
        else:
            obj = Emergency.objects.filter(hospital=Hospital.objects.filter(
                id=Role.objects.filter(employee=request.user.id).first().hospital.id).first())
        return render(request, 'emergs.html', {"emeges": obj, "hospitals": Hospital.objects.all()})
    else:
        return redirect('/einloggen')


def remove_emerg(request, id):
    if request.user.is_authenticated:
        Emergency.objects.filter(case_id=id).delete()
        return redirect('/notfalls')
    else:
        return redirect('/einloggen')


def new_emergx(request):
    if request.user.is_authenticated:
        if Role.objects.filter(employee=request.user.id).first().is_car:
            # list_ids = list(Emergency.objects.values_list('hospital_id', flat = True))
            emgs = Emergency.objects.values_list('hospital_id', flat=True).annotate(total=Count('case_id')).order_by()

            emg_ids = []
            for emg in emgs:
                emg_ids.append(emg)
            hospts = []
            for i in emg_ids:
                hospts += Hospital.objects.filter(id=i)
                #reserved_beds_count = Emergency.objects.filter(hospital_id=i).count()
                print(Emergency.objects.filter(hospital_id=i).count())
            return render(request, 'new_emerg.html',{"hospts": hospts})
        else:
            obj = Emergency.objects.filter(hospital=Hospital.objects.filter(
                id=Role.objects.filter(employee=request.user.id).first().hospital.id).first())
            print(obj.count())
        return render(request, 'new_emerg.html', {"emeges": obj})
    else:
        return redirect('/einloggen')

def new_emerg(request):
    if request.user.is_authenticated:
        if Role.objects.filter(employee=request.user.id).first().is_car:

            hospitals = Hospital.objects.all()
            print(hospitals)
            return render(request, 'new_emerg.html',{"hospts": hospitals})
        else:
            hospitals = Hospital.objects.filter(id=Role.objects.filter(employee=request.user.id).first().hospital.id)
            return render(request, 'new_emerg.html', {"hospts": hospitals})
    else:
        return redirect('/einloggen')


def reserv_emerg(request, id):
    if request.user.is_authenticated:
        emerg_count = Emergency.objects.filter(hospital_id=id).count()
        print(emerg_count)
        if emerg_count < Hospital.objects.filter(id=id).first().beds_count:
            new_emerg = Emergency(hospital_id=id)
            new_emerg.save()
        else:
            return render(request, 'new_emerg.html', {"error": "Kein Bett verfügbar"})

        return redirect('/notfalls')
    else:
        return redirect('/einloggen')