from django.shortcuts import render
from Articles.views import getBase
from Vitrine.models import *


# Create your views here.
def accueil(request):
    return render(request, "Vitrine/accueil.html", getBase(request))

def contact(request):
    return render(request, "Vitrine/contact.html", getBase(request))

def nous(request):
    Bureau = MembreBureau.objects.all()
    Poles = PoleBureau.objects.all()
    for Bureaud in Bureau:
        print(str(Bureaud.CategorieRole))
    context = {'Bureau':Bureau,'Poles':Poles}
    return render(request, "Vitrine/nous.html", getBase(request)|context)

def histoire(request):
    return render(request, "Vitrine/histoire.html", getBase(request))

def partenaires(request):
    return render(request, "Vitrine/partenaires.html", getBase(request))

def sdl(request):
    return render(request, "Vitrine/sdl.html", getBase(request))

def cordees(request):
    return render(request, "Vitrine/cordees.html", getBase(request))

def actionscampus(request):
    return render(request, "Vitrine/actionscampus.html", getBase(request))

def notrecampus(request):
    return render(request, "Vitrine/notrecampus.html", getBase(request))
