from django.db import models

# Create your models here.
class Classe(models.Model):
	nom = models.CharField(max_length=20)
	priorite = models.FloatField(default=0)

	class Meta:
		ordering = ['priorite']

	def __str__(self):
		return self.nom

class Matiere(models.Model):
	nom = models.CharField(max_length=20)
	priorite = models.FloatField(default=0)

	class Meta:
		ordering = ['priorite']

	def __str__(self):
		return self.nom


class Cours(models.Model):
	matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, null=True, blank=True)
	nom = models.CharField(max_length=20)
	priorite = models.FloatField(default=0)
	desc = models.TextField(null=True, blank=True)
	text = models.TextField(null=True, blank=True)
	img = models.ImageField(upload_to='img', null=True, blank=True)
	niveau = models.ManyToManyField(Classe)
	cree = models.DateTimeField(auto_now_add=True)
	modif = models.DateTimeField(auto_now_add=True)
	public = models.BooleanField(default=False)
	estCours = models.BooleanField(default=True)

	@property
	def classes(self):
		return self.niveau.all()

	def fichiers(self):
		return self.fichier_set.all()

	class Meta:
		ordering = ['priorite']

	@property
	def safetext(self):
		return self.text.replace("'", "\\'")

	def __str__(self):
		return self.nom


class Fichier(models.Model):
	nom = models.CharField(max_length=50)
	fichier = models.FileField(upload_to='file')
	cour = models.ForeignKey(Cours, on_delete=models.CASCADE)

	def __str__(self):
		return self.nom
