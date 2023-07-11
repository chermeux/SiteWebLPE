from django.forms import ModelForm, CheckboxSelectMultiple
from django import forms
from home.models import *


class CoursForm(ModelForm):
	class Meta:
		model = Cours
		fields = ['matiere', 'nom', 'priorite', 'public', 'estCours', 'desc', 'img', 'niveau', 'text']
		widgets = {'niveau': CheckboxSelectMultiple()}


class FileFieldForm(forms.Form):
	file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class EleveForm(ModelForm):
	class Meta:
		model = Eleve
		fields = ['nom', 'prenom', 'groupe']

class GroupeForm(ModelForm):
	class Meta:
		model = Groupe
		fields = ['nom']
