# Generated by Django 3.2.5 on 2021-08-06 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
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
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('priorite', models.FloatField()),
            ],
            options={
                'ordering': ['priorite'],
            },
        ),
        migrations.DeleteModel(
            name='Cour',
        ),
        migrations.AddField(
            model_name='cours',
            name='matiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.matiere'),
        ),
    ]
