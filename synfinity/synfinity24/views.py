from django.shortcuts import render
from .models import Octave

# Create your views here.
def home(request):
    return render(request, 'home.html')

def octave(request):
    return render(request, 'competitions/octave.html')

def enigma(request):
    return render(request, 'competitions/enigma.html')

def logoLegends(request):
    return render(request, 'competitions/logo-legends.html')

def tetrarealm(request):
    return render(request, 'competitions/tetrarealm.html')

def imaginArte(request):
    return render(request, 'competitions/imagin-arte.html')

def resonance(request):
    return render(request, 'competitions/resonance.html')

def vortexVentures(request):
    return render(request, 'competitions/vortex-ventures.html')

def octaveReg(request):
    if request.method == "POST":
        schoolName = request.POST['sklName']
        schoolEmail = request.POST['sklEmail']
        accTeacher = request.POST['accTeach']
        teamName = request.POST['teamName']
        std1Name = request.POST['std1Name']
        std2Name = request.POST['std2Name']
        std3Name = request.POST['std3Name']
        std4Name = request.POST['std4Name']
        std1Class = request.POST['std1Class']
        std2Class = request.POST['std2Class']
        std3Class = request.POST['std3Class']
        std4Class = request.POST['std4Class']
        teamEmail = request.POST['teamEmail']
        teacherEmail = request.POST['teachEmail']

        newOctave = Octave(schoolName=schoolName, schoolEmail=schoolEmail, accTeacher=accTeacher, teamName=teamName, std1Name=std1Name, std2Name=std2Name, std3Name=std3Name, std4Name=std4Name, std1Class=std1Class, std2Class=std2Class, std3Class=std3Class, std4Class=std4Class, teamEmail=teamEmail, teacherEmail=teacherEmail)
        newOctave.save()

    return render(request, 'registrations/octave.html')

def enigmaReg(request):
    return render(request, 'registrations/enigma.html')

def logoLegendsReg(request):
    return render(request, 'registrations/logo-legends.html')

def tetrarealmReg(request):
    return render(request, 'registrations/tetrarealm.html')

def imaginArteReg(request):
    return render(request, 'registrations/imagin-arte.html')

def resonanceReg(request):
    return render(request, 'registrations/resonance.html')

def vortexVenturesReg(request):
    return render(request, 'registrations/vortex-ventures.html')

def register(request):
    return render(request, 'register.html')
