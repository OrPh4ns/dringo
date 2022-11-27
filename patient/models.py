from django.db import models


class Patient(models.Model):
    ins_nr = models.IntegerField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    arrival_mode = models.IntegerField()
    pain = models.BooleanField(default=False)
    injury = models.BooleanField(default=False)
    mental = models.IntegerField()
    issue = models.TextField()
    pain_rate = models.IntegerField()
    systole = models.IntegerField()
    diastole = models.IntegerField()
    heart_raet = models.IntegerField()
    breathing_rate = models.IntegerField()
    body_temp = models.IntegerField()
    process_done = models.BooleanField(default=False)