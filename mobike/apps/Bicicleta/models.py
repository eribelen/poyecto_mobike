from django.db import models

# Create your models here.
MENTENCION_CHOICE = [(1,'Si'),(2,'No')]
COMUNA_CHOICES = [
    (0,'Comuna'),
    (1,'La Reina'),
    (2, 'Ñuñoa'),
    (3,'Providencia'),
]

class Bicicleta(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=20)
    mantencion = models.BooleanField(choices=MENTENCION_CHOICE, default=1, blank=False)

    def __str__(self):
        return self.marca

class Estacionamiento(models.Model):
    bicicleta = models.ForeignKey(Bicicleta, null=True, blank=True, on_delete=models.CASCADE)
    comuna = models.CharField(max_length=15, choices=COMUNA_CHOICES, default=0)
    bicicletasDisponibles = models.IntegerField()
    direccion = models.TextField()

    def __str__(self):
        return self.comuna
