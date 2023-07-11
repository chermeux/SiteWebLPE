"""lpeweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import accueil_view, matieres_view, orientation_view, cordees_view, projets_view, contact_view

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueil_view, name='accueil'),
	path('matieres', matieres_view, name='matieres'),
    path('orientation', orientation_view, name='orientation'),
    path('cordees-de-la-reussite', cordees_view, name='cordees'),
    path('projets', projets_view, name='projets'),
    path('contact', contact_view, name='contact'),    
]
