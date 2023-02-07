from django.forms import ModelForm, CheckboxSelectMultiple
from django import forms
from GestionEleves.models import *

class EleveForm(ModelForm):
	class Meta:
		model = Eleve
		fields = ['nom', 'prenom', 'groupe']

class GroupeForm(ModelForm):
	class Meta:
		model = Groupe
		fields = ['nom']
