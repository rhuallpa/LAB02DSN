from django.db import models

class Persona(models.Model):
    id_persona = models.CharField(primary_key=True, max_length=8)
    dni = models.CharField(max_length=8, default='777777')
    apellidos = models.CharField(max_length=100, default='Apellidos')
    nombres = models.CharField(max_length=50, default='predeterminada')
    telefono = models.CharField(max_length=10, default='77')
    email = models.CharField(max_length=100, default=' predeterminada')
    direccion = models.CharField(max_length=100, default='Dirección predeterminada' )
 
    def __str__(self):
        return f"{self.apellidos}, {self.nombres}"
