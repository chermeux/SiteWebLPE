# Generated by Django 4.1.2 on 2022-10-12 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vitrine', '0005_remove_membrebureau_categorierole_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomImage', models.CharField(max_length=50)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]