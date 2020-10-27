from django.db import models
from ..Estacionamiento.models import Estacionamiento

# Create your models here.
MENTENCION_CHOICE = [('si','Si'),('no','No')]

class Bicicleta(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=20)
    mantencion = models.CharField(max_length=2,choices=MENTENCION_CHOICE, default='no')
    estacionamiento = models.ForeignKey(Estacionamiento, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.marca
