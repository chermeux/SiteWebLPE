from django.test import TestCase
from .models import Groupe, Eleve, Appelle, Status
from datetime import date

class GroupeTestCase(TestCase):
    def setUp(self):
        # Crée un groupe pour être utilisé dans les tests
        self.groupe = Groupe.objects.create(nom="Groupe A")

    def test_nom_groupe(self):
        # Vérifie que le nom du groupe créé dans setUp est correct
        self.assertEqual(self.groupe.nom, "Groupe A")


class EleveTestCase(TestCase):
    def setUp(self):
        # Crée un groupe pour être utilisé dans les tests
        self.groupe = Groupe.objects.create(nom="Groupe A")
        # Crée un élève pour être utilisé dans les tests
        self.eleve = Eleve.objects.create(nom="Durand", prenom="Jean", groupe=self.groupe)

    def test_nom_eleve(self):
        # Vérifie que le nom de l'élève créé dans setUp est correct
        self.assertEqual(self.eleve.nom, "Durand")

    def test_prenom_eleve(self):
        # Vérifie que le prénom de l'élève créé dans setUp est correct
        self.assertEqual(self.eleve.prenom, "Jean")

    def test_groupe_eleve(self):
        # Vérifie que le groupe de l'élève créé dans setUp est correct
        self.assertEqual(self.eleve.groupe, self.groupe)


class AppelleTestCase(TestCase):
    def setUp(self):
        # Crée un groupe pour être utilisé dans les tests
        self.groupe = Groupe.objects.create(nom="Groupe A")
        # Crée un appel pour être utilisé dans les tests
        self.appelle = Appelle.objects.create(date=date.today(), groupe=self.groupe)

    def test_date_appelle(self):
        # Vérifie que la date de l'appel créé dans setUp est correcte
        self.assertEqual(self.appelle.date, date.today())

    def test_groupe_appelle(self):
        # Vérifie que le groupe de l'appel créé dans setUp est correct
        self.assertEqual(self.appelle.groupe, self.groupe)


class StatusTestCase(TestCase):
    def setUp(self):
        # Crée un groupe pour être utilisé dans les tests
        self.groupe = Groupe.objects.create(nom="Groupe A")
        # Crée un élève pour être utilisé dans les tests
        self.eleve = Eleve.objects.create(nom="Durand", prenom="Jean", groupe=self.groupe)
        # Crée un appel pour être utilisé dans les tests
        self.appelle = Appelle.objects.create(date=date.today(), groupe=self.groupe)
        # Crée un statut pour être utilisé dans les tests
        self.status = Status.objects.create(eleve=self.eleve, appelle=self.appelle, present=True)

    def test_eleve_status(self):
        # Vérifie que l'élève du statut créé dans setUp est correct
        self.assertEqual(self.status.eleve, self.eleve)

    def test_appelle_status(self):
        # Vérifie que l'appel du statut créé dans setUp est correct
        self.assertEqual(self.status.appelle, self.appelle)

    def test_present_status(self):
        # Vérifie que le statut de présence du statut créé dans setUp est correct
        self.assertEqual(self.status.present, True)
