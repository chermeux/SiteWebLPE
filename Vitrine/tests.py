from django.test import TestCase
from .models import Carrousel, PoleBureau, MembreBureau

class CarrouselModelTest(TestCase):
    def setUp(self):
        # Créer un objet Carrousel
        Carrousel.objects.create(NomImage='testimage', Photo='test.jpg')

    def test_nom_image_label(self):
        # Récupérer l'objet Carrousel créé et tester si le champ NomImage est correct
        carrousel = Carrousel.objects.get(id=1)
        field_label = carrousel._meta.get_field('NomImage').verbose_name
        self.assertEquals(field_label, 'NomImage')

    def test_photo_label(self):
        # Récupérer l'objet Carrousel créé et tester si le champ Photo est correct
        carrousel = Carrousel.objects.get(id=1)
        field_label = carrousel._meta.get_field('Photo').verbose_name
        self.assertEquals(field_label, 'Photo')

    def test_nom_image_max_length(self):
        # Récupérer l'objet Carrousel créé et tester si la longueur maximale de NomImage est correcte
        carrousel = Carrousel.objects.get(id=1)
        max_length = carrousel._meta.get_field('NomImage').max_length
        self.assertEquals(max_length, 50)

class PoleBureauModelTest(TestCase):
    def setUp(self):
        # Créer un objet PoleBureau
        PoleBureau.objects.create(Designation='testdesign', DescriptionPole='test description')

    def test_designation_label(self):
        # Récupérer l'objet PoleBureau créé et tester si le champ Designation est correct
        polebureau = PoleBureau.objects.get(id=1)
        field_label = polebureau._meta.get_field('Designation').verbose_name
        self.assertEquals(field_label, 'Designation')

    def test_description_pole_label(self):
        # Récupérer l'objet PoleBureau créé et tester si le champ DescriptionPole est correct
        polebureau = PoleBureau.objects.get(id=1)
        field_label = polebureau._meta.get_field('DescriptionPole').verbose_name
        self.assertEquals(field_label, 'DescriptionPole')

    def test_designation_max_length(self):
        # Récupérer l'objet PoleBureau créé et tester si la longueur maximale de Designation est correcte
        polebureau = PoleBureau.objects.get(id=1)
        max_length = polebureau._meta.get_field('Designation').max_length
        self.assertEquals(max_length, 50)

class MembreBureauModelTest(TestCase):
    def setUp(self):
        # Créer un objet MembreBureau
        membre = MembreBureau.objects.create(Prenom='testprenom', Nom='testnom', Photo='test.jpg',
                                             Role='testrole', DefinitionRole='testdefinition')

        # Créer un objet PoleBureau
        pole = PoleBureau.objects.create(Designation='testdesign', DescriptionPole='test description')

        # Associer l'objet PoleBureau à l'objet MembreBureau
        membre.CategorieRole = pole
        membre.save()

    def test_prenom_label(self):
        # Récupérer l'objet MembreBureau créé et tester si le champ Prenom est correct
        membre = MembreBureau.objects.get(id=1)
        field_label = membre._meta.get_field('Prenom')
