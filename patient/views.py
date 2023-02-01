from django.shortcuts import render, redirect

import patient
from hospital.models import Hospital
from patient.models import Patient
from role.models import Role

import pandas as pd
import joblib


def patient_call(request):
    return render(request, 'call.html',
                  {"patient": Patient.objects.filter(process_done=True).order_by('-archive_date').values().first()})


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
        patient.archive_date = patient.archive_date.now()
        patient.save()
        patient_count = int(Patient.objects.filter(process_done=0).count())
        if patient_count == 0:
            return redirect('/neuer_patient')
        return redirect('/patienten')
    else:
        return redirect('/einloggen')


def get_patients(request):
    if request.user.is_authenticated:
        if Role.objects.filter(employee=request.user.id).first().is_car:
            patients = Patient.objects.filter(process_done=False).values()
            df = pd.DataFrame.from_dict(patients)
            df.reset_index(drop=True, inplace=True)
        else:
            patients = Patient.objects.filter(process_done=False, hospital=Hospital.objects.filter(
                id=Role.objects.filter(employee=request.user.id).first().hospital.id).first()).values()
            df = pd.DataFrame.from_dict(patients)
            df.reset_index(drop=True, inplace=True)
        df2 = df.iloc[:, 4:15]
        model = joblib.load('model.sav')
        triage = model.predict(df2.values)
        df['Stufe'] = triage
        df = df.sort_values(by=['Stufe'], ascending=[False])
        liste = df.values.tolist()
        return render(request, 'patients.html', {"patients": liste})
    else:
        return redirect('/einloggen')


def archive_patient(request, id):
    return render(request, 'patient.html', {'patient_id': id})


def delete(request, person_pk):
    print(person_pk)


def new_patient(request):
    if request.method == 'POST':
        ins_nr = request.POST['ins_nr']
        # arrival_mode = request.POST['arrival_mode']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        if "exercise_angina" in request.POST:
            exercise_angina = request.POST['exercise_angina']
            if exercise_angina == 'on':
                exercise_angina = 1
            else:
                exercise_angina = 0
        else:
            exercise_angina = 0

        if "heart_disease" in request.POST:
            heart_disease = request.POST['heart_disease']
            if heart_disease == 'on':
                heart_disease = 1
            else:
                heart_disease = 0
        else:
            heart_disease = 0

        if "hypertension" in request.POST:
            hypertension = request.POST['hypertension']
            if hypertension == 'on':
                hypertension = 1
            else:
                hypertension = 0
        else:
            hypertension = 0

        chest_pain_type = request.POST['chest_pain_type']
        blood_pressure = request.POST['blood_pressure']
        max_heart_rate = request.POST['max_heart_rate']
        plasma_glucose = request.POST['plasma_glucose']
        insulin = request.POST['insulin']
        bmi = request.POST['bmi']
        diabetes_pedigree = request.POST['diabetes_pedigree']
        cholesterol = request.POST['cholesterol']

        # .objects.get(id = id)

        patient_data = Patient(ins_nr=ins_nr, firstname=firstname, lastname=lastname, chest_pain_type=chest_pain_type,
                               exercise_angina=exercise_angina, heart_disease=heart_disease, hypertension=hypertension,
                               blood_pressure=blood_pressure, max_heart_rate=max_heart_rate,
                               plasma_glucose=plasma_glucose, insulin=insulin
                               , bmi=bmi, diabetes_pedigree=diabetes_pedigree, cholesterol=cholesterol,
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
