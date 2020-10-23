from django.db import models

# Create your models here.
MENTENCION_CHOICE = [(1,'Si'),(2,'No')]

class Bicicleta(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=20)
    mantencion = models.BooleanField(max_length=2,choices=MENTENCION_CHOICE) # Corregir opción no

    def __str__(self):
        return self.marca
