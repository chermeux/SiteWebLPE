from django.db import models
# Create your models here.

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
