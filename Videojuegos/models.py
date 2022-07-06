from django.db import models

# Create your models here.

class Videojuego(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    genero = models.CharField(max_length=50)
    valoracion = models.IntegerField()