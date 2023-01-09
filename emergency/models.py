from django.db import models
from django.contrib.auth.models import User

from hospital.models import Hospital


class Emergency(models.Model):
    # name = models.CharField(max_length=300, unique=True)
    case_id = models.AutoField(primary_key=True)
    hospital = models.ForeignKey(Hospital, related_name='emergencies', on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str("id = "+str(self.case_id)+" | Hospital =  "+str(self.hospital))