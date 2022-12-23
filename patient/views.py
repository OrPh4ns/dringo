from django.shortcuts import render, redirect

from hospital.models import Hospital
from patient.models import Patient
from role.models import Role


def patient_call(request):
    return render(request, 'call.html', {"patient":Patient.objects.filter(process_done=True).last()})


def get_patient(request, id):
    if request.user.is_authenticated:
        return render(request, 'patient.html', {"patient": Patient.objects.filter(id=id).first()})
    else:
        return redirect('/einloggen')


def reserv_patient(request, id):
    if request.user.is_authenticated:
        print(id)
        patient = Patient.objects.filter(id=id).first()
        patient.process_done = 1
        patient.save()
        return redirect('/patienten')
    else:
        return redirect('/einloggen')


def get_patients(request):
    if request.user.is_authenticated:
        if Role.objects.filter(employee=request.user.id).first().is_car:
            patients = Patient.objects.filter(process_done=False)
        else:
            patients = Patient.objects.filter(process_done=False,hospital=Hospital.objects.filter(
                id=Role.objects.filter(employee=request.user.id).first().hospital.id).first())

        return render(request, 'patients.html', {"patients": patients})
    else:
        return redirect('/einloggen')

def archive_patient(request, id):
    print(id)
    return render(request, 'patient.html', {'patient_id': id})

def delete(request, person_pk):
    print(person_pk)

def new_patient(request):
    if request.method == 'POST':
        ins_nr = request.POST['ins_nr']
        arrival_mode = request.POST['arrival_mode']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        if "pain" in request.POST:
            pain = request.POST['pain']
            if pain == 'on':
                pain = True
            else:
                pain = False
        else:
            pain = False

        if "injury" in request.POST:
            injury = request.POST['injury']
            if injury == 'on':
                injury = True
            else:
                injury = False
        else:
            injury = False

        mental = request.POST['mental']
        pain_rate = request.POST['pain_rate']
        systole = request.POST['systole']
        diastole = request.POST['diastole']
        heart_raet = request.POST['heart_raet']
        breathing_rate = request.POST['breathing_rate']
        body_temp = request.POST['body_temp']

        # .objects.get(id = id)

        patient_data = Patient(ins_nr=ins_nr, arrival_mode=arrival_mode, firstname=firstname, lastname=lastname,
                               pain=pain, injury=injury, mental=mental, pain_rate=pain_rate, systole=systole,
                               diastole=diastole, heart_raet=heart_raet
                               , breathing_rate=breathing_rate, body_temp=body_temp,
                               hospital=Hospital.objects.filter(
                                   id=Role.objects.filter(employee=request.user.id).first().hospital.id).first())
        if patient_data.save():
            return redirect('/patienten')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'login.html', {'error_message': 'Falsche Daten'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'new_patient.html')
