from django.shortcuts import render

# Create your views here.

def accueil_view(request, titre= 'Accueil'):
	return render(request, "accueil.html", {'titre': titre})

def matieres_view(request, titre= 'Mes Matières'):
	return render(request, "matieres.html", {'titre': titre})

def orientation_view(request, titre= "S'orienter"):
	return render(request, "orientation.html", {'titre': titre})

def cordees_view(request, titre= 'Interventions Cordées'):
	return render(request, "cordees.html", {'titre': titre})

def projets_view(request, titre= 'Mes Projets'):
	return render(request, "projets.html", {'titre': titre})

def contact_view(request, titre= 'Contactez-nous'):
	return render(request, "contact.html", {'titre': titre})