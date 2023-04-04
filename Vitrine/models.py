from django.db import models

# Modèle pour stocker les images du carrousel sur la page d'accueil
class Carrousel(models.Model):
    # Nom de l'image affiché sur le carrousel
    NomImage = models.CharField(max_length=50)
    # Image à afficher
    Photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        # Affichage du nom de l'image
        return self.NomImage

# Modèle pour stocker les différents pôles et leurs descriptions
class PoleBureau(models.Model):
    # Nom du pôle
    Designation = models.CharField(max_length=50)
    # Description du pôle
    DescriptionPole = models.TextField(null=True)

    def __str__(self):
        # Affichage de la désignation du pôle
        return self.Designation

# Modèle pour stocker les membres du bureau
class MembreBureau(models.Model):
    # Prénom du membre
    Prenom = models.CharField(max_length=50)
    # Nom du membre
    Nom = models.CharField(max_length=50)
    # Photo du membre
    Photo = models.FileField()
    # Rôle du membre
    Role = models.CharField(max_length=50)
    # Pôle dans lequel se situe le membre
    CategorieRole = models.ForeignKey(PoleBureau, null=True, on_delete=models.SET_NULL)
    # Description du rôle du membre
    DefinitionRole = models.CharField(max_length=50)
    # Lien vers le compte Facebook du membre
    FaceBook = models.TextField(null=True)
    # Lien vers le compte Instagram du membre
    Instagram = models.TextField(null=True)
    # Lien vers le compte Linkedin du membre
    Linkedin = models.TextField(null=True)

    def __str__(self):
        # Affichage du rôle du membre
        return self.Role
