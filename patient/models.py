from django.db import models

from hospital.models import Hospital


class Patient(models.Model):
    ins_nr = models.IntegerField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    chest_pain_type = models.IntegerField()
    blood_pressure = models.IntegerField()
    cholesterol = models.IntegerField()
    max_heart_rate = models.IntegerField()
    exercise_angina = models.IntegerField(default=0)
    plasma_glucose = models.IntegerField()
    insulin = models.IntegerField()
    bmi = models.FloatField()
    diabetes_pedigree = models.FloatField()
    hypertension = models.IntegerField(default=0)
    heart_disease = models.IntegerField(default=0)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    process_done = models.BooleanField(default=False)
    archive_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname+ " " + self.lastname