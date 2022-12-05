from django.db import models

from hospital.models import Hospital


class Patient(models.Model):
    ins_nr = models.IntegerField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    arrival_mode = models.IntegerField()
    pain = models.BooleanField(default=False)
    injury = models.BooleanField(default=False)
    mental = models.IntegerField()
    pain_rate = models.IntegerField()
    systole = models.IntegerField()
    diastole = models.IntegerField()
    heart_raet = models.IntegerField()
    breathing_rate = models.IntegerField()
    body_temp = models.IntegerField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    process_done = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname+ " " + self.lastname