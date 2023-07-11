# Generated by Django 3.2.5 on 2021-08-06 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('priorite', models.FloatField()),
            ],
            options={
                'ordering': ['priorite'],
            },
        ),
        migrations.CreateModel(
            name='Cour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.classe')),
            ],
        ),
    ]