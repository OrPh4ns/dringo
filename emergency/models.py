from django.db import models
from django.contrib.auth.models import User

from hospital.models import Hospital


class Emergency(models.Model):
    #name = models.CharField(max_length=300, unique=True)
    description = models.CharField(max_length=150)
    hospital = models.ForeignKey(Hospital, related_name='emergencies', on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)