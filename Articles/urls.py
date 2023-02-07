from django.contrib import admin
from django.urls import path, include
from Articles.views import *


urlpatterns = [
    path('college/', college),
    path('lycee/', lycee),
    path('matieres/', matieres, {'id': None}),
    path('matieres/<int:id>/', matieres),
    path('orientation/', orientation),
    path('cours/<int:id>/', cours),
    path('ad/cours/<int:id>/', coursAdmin),
    path('ad/cours/', coursAdmin, {'id': None}),
    path('fichier/delete/<int:id>', deleteFile),
]
