from django.db import models

# Create your models here.
class Octave(models.Model):
    schoolName = models.CharField(max_length=200)
    schoolEmail = models.CharField(max_length=200)
