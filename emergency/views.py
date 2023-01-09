from django.db import connection
from django.db.models import Count
from django.shortcuts import render, redirect

from emergency import models
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
            free_bed_hospital = []
            for p in Hospital.objects.raw('''SELECT *
FROM hospital_hospital h
WHERE h.id not in (select e.hospital_id from emergency_emergency e) or h.id in 
(select e.hospital_id from emergency_emergency e 
where e.hospital_id = h.id group by e.hospital_id  having count(*)<h.beds_count);'''):
                free_bed_hospital.append(p)
            return render(request, 'new_emerg.html', {"hospts": free_bed_hospital})
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
            all_hospitals = Hospital.objects.all()
            all_emergs = Emergency.objects.all()
            return render(request, 'new_emerg.html', {"hospts": hospitals})
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
