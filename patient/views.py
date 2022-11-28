from django.shortcuts import render


def patient_call(request):
    return render(request, 'call.html')


def get_patient(request):
    return render(request, 'patient.html')

def get_patients(request):
    return render(request, 'patients.html')
