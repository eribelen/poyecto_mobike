from django import forms
from .models import Estacionamiento

COMUNA_CHOICES = [
    ('Sin Comuna','Seleccione Comuna'),
    ('La Reina','La Reina'),
    ('Ñuñoa', 'Ñuñoa'),
    ('Providencia','Providencia'),
]

class EstacionamientoForm(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = ['comuna', 'direccion', 'bicicletasDisponibles']
        labels = {
            'comuna': 'Comuna',
            'direccion': 'Dirección',
            'bicicletasDisponibles': 'Bicicletas disponibles',
        }
        widgets = {
            'comuna': forms.Select(choices=COMUNA_CHOICES, attrs={'class': 'mb-2 form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'mb-2 form-control'}),
            'bicicletasDisponibles': forms.NumberInput(attrs={'class': 'mb-2 form-control'}),
        }