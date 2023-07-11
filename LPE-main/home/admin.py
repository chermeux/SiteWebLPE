from django.contrib import admin
from home   .models import Classe, Cours, Matiere, Fichier


# Register your models here.
admin.site.register(Classe)
admin.site.register(Cours)
admin.site.register(Matiere)
admin.site.register(Fichier)
