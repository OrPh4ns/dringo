from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=300, unique=True)
    beds_count = models.IntegerField()
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
