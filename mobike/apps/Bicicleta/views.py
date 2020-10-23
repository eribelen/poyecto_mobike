from django.shortcuts import render
from .models import Bicicleta

# Create your views here.
def listar_bicicletas(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, "Bicicleta/listar_bicicletas.html", {'bicicletas': bicicletas})
