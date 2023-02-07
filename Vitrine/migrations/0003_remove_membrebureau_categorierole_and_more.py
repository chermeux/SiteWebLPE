# Generated by Django 4.1.2 on 2022-10-11 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vitrine', '0002_polebureau_remove_membrebureau_categorierole_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membrebureau',
            name='CategorieRole',
        ),
        migrations.AddField(
            model_name='membrebureau',
            name='CategorieRole',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vitrine.polebureau'),
        ),
    ]