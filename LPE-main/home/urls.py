from django.contrib import admin
from django.urls import path

from home.views import *

urlpatterns = [
    path('', accueil),
	path('matieres/', matieres, {'id': None}),
    path('matieres/<int:id>/', matieres),
    path('orientation/', orientation),
    path('cordees/', cordees),
    path('cordees-de-la-reussite/', cordees),
    path('projets/', projets),
    path('contact/', contact),
    path('cours/<int:id>/', cours),
    path('ad/cours/<int:id>/', coursAdmin),
    path('ad/cours/', coursAdmin, {'id': None}),
    path('fichier/delete/<int:id>', deleteFile),
    path('login/', loginPage),
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
    path('getAppel/', getxl)
]
