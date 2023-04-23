from django.db import models
from GestionEleves.models import Eleve
from GestionEleves.models import Groupe


# Create your models here.


class Tuteur(models.Model):
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=50)
	groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)


class Eleves(models.Model):
	id_eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)