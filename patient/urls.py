from django.urls import path

from patient import views

urlpatterns = [
    path('call', views.patient_call, name='patient_call'),
    path('patient', views.get_patient, name='get_patient'),
    path('patients', views.get_patients, name='get_patients')
    # path('info', views.get_info, name='info'),
]
