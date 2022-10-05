from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_de_creacion = models.DateField()
    edad = models.IntegerField()
    