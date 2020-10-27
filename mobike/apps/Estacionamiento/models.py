from django.db import models

# Create your models here.
COMUNA_CHOICES = [
    ('Sin Comuna','Seleccione Comuna'),
    ('La Reina','La Reina'),
    ('Ñuñoa', 'Ñuñoa'),
    ('Providencia','Providencia'),
]

class Estacionamiento(models.Model):
    comuna = models.CharField(max_length=15, choices=COMUNA_CHOICES, default='Sin Comuna')
    direccion = models.TextField()
    bicicletasDisponibles = models.IntegerField()

    def __str__(self):
        return self.direccion