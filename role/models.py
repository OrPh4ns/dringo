from django.contrib.auth.models import User
from django.db import models

from hospital.models import Hospital


class Role(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    is_car = models.BooleanField(default=False)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.hospital) + " | " + str(self.employee) + " | Wagen = " + str(self.is_car)