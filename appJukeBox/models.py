from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

class Banda(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()
    estilos = models.ManyToManyField("Estilo", null=True)

class Estilo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()