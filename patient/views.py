from django.shortcuts import render

from patient.models import Patient


def patient_call(request):
    return render(request, 'call.html')


def get_patient(request):
    return render(request, 'patient.html')


def get_patients(request):

    return render(request, 'patients.html')


def new_patient(request):
    return render(request, 'new_patient.html')
