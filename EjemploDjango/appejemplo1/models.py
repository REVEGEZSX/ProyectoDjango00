from django.db import models

# Create your models here.
class Libro(models.Model):
    name = models.CharField(max_length = 20)
    author = models.CharField(max_length = 20)
    campoActivo = models.BooleanField
class estante(models.Model):
    fila = models.IntegerField
    columna = models.IntegerField
    campoActivo = models.BooleanField
class prestamo(models.Model):
    fechaPrestamo = models.DateTimeField
    fechaEntrega = models.DateField
    campoActivo = models.BooleanField
class cliente(models.Model):
    nombreCliente = models.CharField(max_length = 20)
    apellidoCliente = models.CharField(max_length = 20)
