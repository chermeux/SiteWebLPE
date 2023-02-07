from django.db import models

# Create your models here.
class Carrousel(models.Model):
    NomImage = models.CharField(max_length=50)
    Photo = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.NomImage

class PoleBureau(models.Model):
    Designation = models.CharField(max_length=50)
    DescriptionPole = models.TextField(null=True)
    def __str__(self):
        return self.Designation

class MembreBureau(models.Model):
    Prenom = models.CharField(max_length=50)
    Nom = models.CharField(max_length=50)
    Photo = models.FileField()
    Role = models.CharField(max_length=50)
    CategorieRole = models.ForeignKey(PoleBureau,null=True,on_delete=models.SET_NULL)
    DefinitionRole = models.CharField(max_length=50)
    FaceBook = models.TextField(null=True)
    Instagram = models.TextField(null=True)
    Linkedin = models.TextField(null=True)
    def __str__(self):
        return self.Role
