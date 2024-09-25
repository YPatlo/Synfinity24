from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("register", views.register, name='register'),
    path("competitions/octave", views.octave, name='octave'),
    path("competitions/enigma", views.enigma, name='enigma'),
    path("competitions/logo-legends", views.logoLegends, name='logoLegends'),
    path("competitions/imagin-arte", views.imaginArte, name='imaginArte'),
    path("competitions/tetrarealm", views.tetrarealm, name='tetrarealm'),
    path("competitions/resonance", views.resonance, name='resonace'),
    path("competitions/vortex-ventures", views.vortexVentures, name='votexVentures'),
    path("registrations/octave", views.octaveReg, name='octaveReg'),
    path("registrations/enigma", views.enigmaReg, name='enigmaReg'),
    path("registrations/logo-legends", views.logoLegendsReg, name='logoLegendsReg'),
    path("registrations/imagin-arte", views.imaginArteReg, name='imaginArteReg'),
    path("registrations/tetrarealm", views.tetrarealmReg, name='tetrarealmReg'),
    path("registrations/resonance", views.resonanceReg, name='resonaceReg'),
    path("registrations/vortex-ventures", views.vortexVenturesReg, name='votexVenturesReg'),
    path("_", views.reload, name='reload'),
]
