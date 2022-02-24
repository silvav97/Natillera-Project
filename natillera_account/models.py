from pyexpat import model
from django.db import models

# Create your models here.


class Natillera(models.Model):
    name = models.CharField(max_length=100)
    monthlyfee = models.FloatField()

    def __str__(self):
        return self.name