from django.shortcuts import render, redirect

import patient
from hospital.models import Hospital
from patient.models import Patient
from role.models import Role


def patient_call(request):
    return render(request, 'call.html', {"patient":Patient.objects.filter(process_done=True).order_by('-archive_date').values().first()})


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
        import pandas as pd
        import joblib
        df=pd.DataFrame(patients)
        df2=df.iloc[:,4:]
        model = joblib.load('test_model.sav')
        triage= model.predict(df2)
        df['Stufe'] = triage
        df=df.sort_values(by=['Stufe'])
        return render(request, 'patients.html', {"patients": df})
    else:
        return redirect('/einloggen')

def archive_patient(request, id):
    return render(request, 'patient.html', {'patient_id': id})

def delete(request, person_pk):
    print(person_pk)

def new_patient(request):
    if request.method == 'POST':
        ins_nr = request.POST['ins_nr']
        #arrival_mode = request.POST['arrival_mode']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        if "exercise_angina " in request.POST:
            exercise_angina = request.POST['exercise_angina ']
            if exercise_angina == 'on':
                exercise_angina = True
            else:
                exercise_angina = False
        else:
            exercise_angina = False

        if "hypertension " in request.POST:
            hypertension  = request.POST['hypertension ']
            if hypertension  == 'on':
                hypertension  = True
            else:
                hypertension  = False
        else:
            hypertension = False
        
        if "heart_disease " in request.POST:
            heart_disease  = request.POST['heart_disease ']
            if heart_disease  == 'on':
                heart_disease  = True
            else:
                heart_disease  = False
        else:
            heart_disease = False

        chest_pain_type  = request.POST['chest_pain_type ']
        blood_pressure  = request.POST['blood_pressure ']
        cholesterol  = request.POST['cholesterol ']
        max_heart_rate  = request.POST['max_heart_rate ']
        plasma_glucose  = request.POST['plasma_glucose ']
        insulin  = request.POST['insulin ']
        bmi  = request.POST['bmi']
        diabetes_pedigree   = request.POST['diabetes_pedigree ']

        # .objects.get(id = id)

        patient_data = Patient(ins_nr=ins_nr, firstname=firstname, lastname=lastname,
                               chest_pain_type =chest_pain_type , exercise_angina =exercise_angina , hypertension =hypertension , heart_disease =heart_disease , blood_pressure =blood_pressure ,
                               cholesterol =cholesterol , max_heart_rate =max_heart_rate 
                               , plasma_glucose =plasma_glucose , insulin =insulin ,bmi =bmi ,diabetes_pedigree = diabetes_pedigree ,
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
