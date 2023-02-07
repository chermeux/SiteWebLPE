from django.contrib import admin
from django.urls import path

from GestionEleves.views import *

urlpatterns = [
    path('liste/', liste),
    path('newGroupe/', newGroupe),
    path('newEleve/', newEleve),
    path('newAppelle/', newAppelle),
    path('groupe/<int:id>/', groupe),
    path('eleve/<int:id>/', eleve),
    path('appel/<int:id>/', appelle),
    path('deleteGroupe/<int:id>/', deleteGroupe),
    path('deleteEleve/<int:id>/', deleteEleve),
    path('deleteAppelle/<int:id>/', deleteAppelle),
    path('getAppel/', getxl),
]
