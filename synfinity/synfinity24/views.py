from django.shortcuts import render

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
