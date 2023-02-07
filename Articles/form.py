from django.forms import ModelForm, CheckboxSelectMultiple
from django import forms
from Articles.models import *



class CoursForm(ModelForm):
	class Meta:
		model = Cours
		fields = ['matiere', 'nom', 'priorite', 'public', 'estCours','desc', 'img', 'niveau', 'text']
		widgets = {'niveau': CheckboxSelectMultiple()}


class FileFieldForm(forms.Form):
	file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
