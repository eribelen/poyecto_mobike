from django import forms
from .models import Bicicleta

MENTENCION_CHOICE = [(1,'Si'),(2,'No')]

class BicicletaForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = ['marca', 'modelo', 'mantencion', 'estacionamiento']
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'mantencion': 'Mantención',
            'estacionamiento': 'Estacionamiento Asignado',
        }
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'mb-2 form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'mb-2 form-control'}),
            'mantencion': forms.Select(choices=MENTENCION_CHOICE, attrs={'class': 'mb-2 form-control'}),
            'estacionamiento': forms.TextInput(attrs={'class': 'mb-2 form-control'}),
        }