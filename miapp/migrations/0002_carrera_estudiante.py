# Generated by Django 3.0.8 on 2020-08-27 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcarrera', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
                ('nombrecorto', models.CharField(max_length=4)),
                ('fechafundacion', models.DateField()),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idestudiante', models.IntegerField()),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=40)),
                ('dni', models.CharField(max_length=8)),
                ('direccion', models.CharField(max_length=80)),
                ('fechanacimiento', models.DateField()),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
    ]
