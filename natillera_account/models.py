from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Natillera(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    monthlyfee = models.FloatField()

    def __str__(self):
        return self.name
