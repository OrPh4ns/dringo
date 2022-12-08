from django.template.defaulttags import url
from django.urls import path

from patient import views

urlpatterns = [
    path('aufruf', views.patient_call, name='patient_call'),
    path('patient/<int:id>/', views.get_patient, name='get_patient'),
    path('patienten', views.get_patients, name='get_patients'),
    path('neuer_patient', views.new_patient, name='get_patients'),
    path('archive_patient/<int:id>/', views.archive_patient),
    path('reserv/<int:id>/', views.reserv_patient),
    # path('info', views.get_info, name='info'),
]