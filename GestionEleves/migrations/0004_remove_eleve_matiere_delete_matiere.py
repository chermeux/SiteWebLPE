# Generated by Django 4.1.1 on 2023-04-23 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionEleves', '0003_alter_eleve_matiere'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='matiere',
        ),
        migrations.DeleteModel(
            name='Matiere',
        ),
    ]