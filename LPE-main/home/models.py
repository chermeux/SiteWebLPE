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


class Groupe(models.Model):
	nom = models.CharField(max_length=50)

	def __str__(self):
		return self.nom

	@property
	def eleves(self):
		return self.eleve_set.all()

	@property
	def appelles(self):
		return self.appelle_set.all()

class Eleve(models.Model):
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=50)
	groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.nom} {self.prenom} {self.groupe}'

	@property
	def status(self):
		return self.status_set.all()

	@property
	def presence(self):
		appelles = self.groupe.appelles
		l = []
		for appelle in appelles:
			try:
				v = appelle.status_set.get(eleve_id=self.id).present
			except:
				v = None
			l.append(v)
		return l

class Appelle(models.Model):
	date = models.DateField(auto_now_add=True)
	groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.date} {self.groupe}'


class Status(models.Model):
	eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
	appelle = models.ForeignKey(Appelle, on_delete=models.CASCADE)
	present = models.BooleanField()
