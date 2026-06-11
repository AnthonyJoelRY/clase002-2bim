from datetime import date
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()


    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Ciudad: {self.Ciudad()} - Edad: {self.edad} - Año de nacimiento: {self.anio_nacimiento()}"
    
    def anio_nacimiento(self):
        return date.today().year - self.edad
    
    def Ciudad (self):
        if self.cedula.startswith("11"):
            return "Loja"
        else:
            return "Otra ciudad"
