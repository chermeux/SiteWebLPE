from django.contrib import admin
from GestionEleves.models import Groupe, Eleve, Appelle, Status


# Register your models here.
admin.site.register(Groupe)
admin.site.register(Eleve)
admin.site.register(Appelle)
admin.site.register(Status)
