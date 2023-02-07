from django.contrib import admin
from django.urls import path, include
from Vitrine.views import *

urlpatterns = [
    path('', accueil),
    path('histoire/', histoire),
    path('nous/', nous),
    path('partenaires/', partenaires),
    path('sdl/', sdl),
    path('contact/', contact),
    path('cordees/', cordees),
    path('actionscampus/', actionscampus),
    path('notrecampus/', notrecampus),
]
