from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=155)
    age = models.IntegerField()
    gender = models.CharField(max_length=155)
    