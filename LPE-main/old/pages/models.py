from django.db import models

# Create your models here.

class Cours(models.Model):
    titre=models.CharField(max_length=50)
    description=models.TextField()
    image=models.CharField(max_length=2000)
    video=models.CharField(max_length=2000)
    pdf=models.CharField(max_length=2000)

# TO DO rajouter sur la base de données python manage.py makemigrations