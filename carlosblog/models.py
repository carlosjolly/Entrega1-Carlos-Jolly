from django.db import models

# Create your models here.
class Contact(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=200)
    telefono = models.IntegerField()

class Trabajos(models.Model):
    nombre = models.CharField(max_length=40)
    trabajo = models.CharField(max_length=40)

class Alumnos(models.Model):
    nombre = models.CharField(max_length=40)
    cursos = models.CharField(max_length=40)

