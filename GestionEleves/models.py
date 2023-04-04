from django.db import models

# Définition de la classe Groupe
class Groupe(models.Model):
    # Le nom du groupe, stocké dans un champ CharField
    nom = models.CharField(max_length=50)

    # Méthode appelée pour afficher le nom du groupe dans l'administration
    def __str__(self):
        return self.nom

    # Renvoie tous les élèves appartenant à ce groupe
    @property
    def eleves(self):
        return self.eleve_set.all()

    # Renvoie tous les appels pour ce groupe
    @property
    def appelles(self):
        return self.appelle_set.all()

# Définition de la classe Eleve
class Eleve(models.Model):
    # Le nom et le prénom de l'élève
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    # Le groupe auquel appartient l'élève, stocké dans une clé étrangère
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)

    # Méthode appelée pour afficher le nom de l'élève dans l'administration
    def __str__(self):
        return f'{self.nom} {self.prenom} {self.groupe}'

    # Renvoie tous les status de l'élève
    @property
    def status(self):
        return self.status_set.all()

    # Renvoie une liste indiquant si l'élève est présent ou non à chaque appel
    @property
    def presence(self):
        appelles = self.groupe.appelles
        l = []
        for appelle in appelles:
            try:
                v = appelle.status_set.get(eleve_id=self.id).present
            except:
                v = False
            l.append(v)
        return l

# Définition de la classe Appelle
class Appelle(models.Model):
    # La date de l'appel, stockée dans un champ DateField
    date = models.DateField(auto_now_add=True)

    # Le groupe pour lequel l'appel est effectué, stocké dans une clé étrangère
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)

    # Méthode appelée pour afficher la date et le groupe dans l'administration
    def __str__(self):
        return f'{self.date} {self.groupe}'

# Définition de la classe Status
class Status(models.Model):
    # L'élève pour lequel le status est enregistré, stocké dans une clé étrangère
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)

    # L'appel pour lequel le status est enregistré, stocké dans une clé étrangère
    appelle = models.ForeignKey(Appelle, on_delete=models.CASCADE)

    # Indique si l'élève est présent ou non lors de l'appel
    present = models.BooleanField()
