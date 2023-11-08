from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50)


    # Define lo que se muestra en http://127.0.0.1:8000/admin
    def __str__(self):
        return self.nombre

    # Solo utiles para trabajar en shell(es preferible hacer cambios desde la pagina http://127.0.0.1:8000/admin)
    def set_nombre(self,nombre):
        self.nombre = nombre
        return "Nombre",nombre,"asignado" 

class Estilo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()


    # Define lo que se muestra en http://127.0.0.1:8000/admin
    def __str__(self):
        return self.nombre
    
    # Solo utiles para trabajar en shell(es preferible hacer cambios desde la pagina http://127.0.0.1:8000/admin)
    def set_nombre(self, nombre):
        self.nombre = nombre
        return "Nombre",nombre,"asignado"
    
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
        return "descripcion asignada"

class Banda(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()
    estilos = models.ManyToManyField(Estilo)    

    # Define lo que se muestra en http://127.0.0.1:8000/admin
    def __str__(self):
        return self.nombre
    
    # Solo utiles para trabajar en shell(es preferible hacer cambios desde la pagina http://127.0.0.1:8000/admin)
    def set_nombre(self,nombre):
        self.nombre = nombre
        return "Nombre",nombre,"asignado" 
    
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
        return "descripcion asignada"

    def add_estilo(self, estilo):
        self.estilos.add(estilo) 
        return "Estilo",estilo.nombre,"añadido"
    
    def set_pais(self, pais):
        self.pais = pais
        return "Pais",pais,"asignado"

    def set_estiloprincipal(self, estilo_principal):
        self.estilo_principal = estilo_principal    
        return "Estilo principañ", estilo_principal, "asignado"