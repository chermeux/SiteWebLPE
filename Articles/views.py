from datetime import datetime
from django.core.files.temp import NamedTemporaryFile

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Articles.form import *
from Articles.models import *

# Create your views here.
def getBase(request):
    return {'matieres': Matiere.objects.all(), 'user': request.user}

def college(request):
    cours = Cours.objects.filter(estCours=False)
    if not request.user.is_authenticated:
        cours.filter(public=True)
    return render(request, "Articles/college.html", getBase(request) | {'cours': cours})


def lycee(request):
    cours = Cours.objects.filter(estCours=False)
    if not request.user.is_authenticated:
        cours.filter(public=True)
    return render(request, "Articles/lycee.html", getBase(request) | {'cours': cours})

def matieres(request,id):
    if id is None:
        cours = Cours.objects.filter(estCours=True)
    else:
        cours = Cours.objects.filter(matiere_id=id, estCours=True)
    if not request.user.is_authenticated:
        cours.filter(public=True)
    return render(request, "Articles/matieres.html", getBase(request) | {'cours': cours})

def orientation(request):
    cours = Cours.objects.filter(estCours=False)
    if not request.user.is_authenticated:
        cours.filter(public=True)
    return render(request, "Articles/orientation.html", getBase(request) | {'cours': cours})

def cours(request, id):
    return render(request, "Articles/cours.html", getBase(request) | {"cours": Cours.objects.get(id=id)})

@login_required
def coursAdmin(request, id):
    nv = False
    if request.method == 'POST':
        if request.POST['delete'] == 'je veux supprimer ce cours':
            Cours.objects.get(id=id).delete()
            return redirect('/Articles/matieres/')
        if id is not None:
            print(request.POST, request.FILES)
            form = CoursForm(request.POST, request.FILES, instance=Cours.objects.get(id=id))
            cours = form.save()
        else:
            form = CoursForm(request.POST, request.FILES)
            cours = form.save()
            id = cours.id
            nv = True
        files = request.FILES.getlist('file_field')
        for f in files:
            newFile = Fichier(nom=f.name[:40], fichier=f, cour_id=id)
            if newFile.fichier.name.endswith('.pdf'):
                newFile.save()
    if nv:
        return redirect(f'/Articles/ad/cours/{id}')
    return render(request, 'Articles/editCoursAdmin.html', getBase(request) |
                  {"coursForm": CoursForm(instance=Cours.objects.get(id=id)) if id is not None else CoursForm(),
                   'cours': Cours.objects.get(id=id) if id is not None else None,
                   'fileForm': FileFieldForm(use_required_attribute=False)})

@login_required
def deleteFile(request, id):
    fichier = Fichier.objects.get(id=id)
    idCours = fichier.cour_id
    fichier.fichier.delete()
    fichier.delete()
    return redirect(f'/Articles/ad/cours/{idCours}')

@login_required
def deleteCours(request, id):
    cours = Cours.objects.get(id=id)
    cours.delete()
    return redirect('/Articles/matieres/')
