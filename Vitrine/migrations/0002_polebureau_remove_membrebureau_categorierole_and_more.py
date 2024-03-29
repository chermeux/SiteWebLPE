# Generated by Django 4.1.2 on 2022-10-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vitrine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoleBureau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation', models.CharField(max_length=50)),
                ('DescriptionPole', models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='membrebureau',
            name='CategorieRole',
        ),
        migrations.AddField(
            model_name='membrebureau',
            name='CategorieRole',
            field=models.ManyToManyField(to='Vitrine.polebureau'),
        ),
    ]
