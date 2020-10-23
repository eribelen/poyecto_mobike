from django import forms
from .models import Bicicleta

MENTENCION_CHOICE = [(1,'Si'),(2,'No')]

class BicicletaForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = ['marca', 'modelo', 'mantencion']
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'mantencion': 'Mantención',
        }
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'mantencion': forms.Select(choices=MENTENCION_CHOICE, attrs={'class': 'form-control'}),
        }