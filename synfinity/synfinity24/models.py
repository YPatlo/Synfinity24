from django.db import models

# Create your models here.
class Octave(models.Model):
    schoolName = models.TextField()
    schoolEmail = models.TextField()
    accTeacher = models.TextField()
    teamName = models.TextField()
    std1Name = models.TextField()
    std2Name = models.TextField()
    std3Name = models.TextField()
    std4Name = models.TextField()
    std1Class = models.TextField()
    std2Class = models.TextField()
    std3Class = models.TextField()
    std4Class = models.TextField()
    teamEmail = models.TextField()
    teacherEmail = models.TextField()

