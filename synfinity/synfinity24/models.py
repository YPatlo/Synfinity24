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
    def __str__(self):
        return self.schoolName

class Enigma(models.Model):
    schoolName = models.TextField()
    schoolEmail = models.TextField()
    accTeacher = models.TextField()
    teamName = models.TextField()
    std1Name = models.TextField()
    std2Name = models.TextField()
    std1Class = models.TextField()
    std2Class = models.TextField()
    teamEmail = models.TextField()
    teacherEmail = models.TextField()
    def __str__(self):
        return self.schoolName

class LogoLegends(models.Model):
    schoolName = models.TextField()
    schoolEmail = models.TextField()
    accTeacher = models.TextField()
    teamName = models.TextField()
    std1Name = models.TextField()
    std2Name = models.TextField()
    std3Name = models.TextField()
    std1Class = models.TextField()
    std2Class = models.TextField()
    std3Class = models.TextField()
    teamEmail = models.TextField()
    teacherEmail = models.TextField()
    def __str__(self):
        return self.schoolName

class ImaginArte(models.Model):
    schoolName = models.TextField()
    schoolEmail = models.TextField()
    accTeacher = models.TextField()
    teamName = models.TextField()
    std1Name = models.TextField()
    std2Name = models.TextField()
    std1Class = models.TextField()
    std2Class = models.TextField()
    teamEmail = models.TextField()
    teacherEmail = models.TextField()
    def __str__(self):
        return self.schoolName

class VortexVentures(models.Model):
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
    def __str__(self):
        return self.schoolName

class Resonance(models.Model):
    schoolName = models.TextField()
    schoolEmail = models.TextField()
    accTeacher = models.TextField()
    teamName = models.TextField()
    std1Name = models.TextField()
    std2Name = models.TextField()
    std1Class = models.TextField()
    std2Class = models.TextField()
    teamEmail = models.TextField()
    teacherEmail = models.TextField()
    def __str__(self):
        return self.schoolName

class Tetrarealm(models.Model):
    schoolName = models.TextField()
    schoolEmail = models.TextField()
    accTeacher = models.TextField()
    teamName = models.TextField()
    std1Name = models.TextField()
    std2Name = models.TextField()
    std3Name = models.TextField()
    std1Class = models.TextField()
    std2Class = models.TextField()
    std3Class = models.TextField()
    teamEmail = models.TextField()
    teacherEmail = models.TextField()
    def __str__(self):
        return self.schoolName
