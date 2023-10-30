from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Banda(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()
    estilos = models.ManyToManyField("Estilo", null=True)
    
    def __str__(self):
        return self.nombre, self.descripcion
    
    def add_estilo(self, estilo):
        self.estilos.add(estilo) 
        return "Estilo",estilo.nombre,"añadido"
    
    def set_pais(self, pais):
        self.pais = pais
        return "Pais",pais,"asignado"

class Estilo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre, self.descripcion