from django.db import models

# Create your models here.
class Curso(models.Model):
    idcurso = models.IntegerField()
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=120)
    horas = models.CharField(max_length=2)
    creditos = models.IntegerField()
    estado = models.CharField(max_length=1)

class Carrera(models.Model):
    idcarrera = models.IntegerField()
    nombre = models.CharField(max_length=20)
    nombrecorto = models.CharField(max_length=4)
    fechafundacion = models.DateField()
    estado = models.CharField(max_length=1)

class Estudiante(models.Model):
    idestudiante = models.IntegerField()
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    dni = models.CharField(max_length=8)
    direccion = models.CharField(max_length=80)
    fechanacimiento = models.DateField()
    estado = models.CharField(max_length=1)
