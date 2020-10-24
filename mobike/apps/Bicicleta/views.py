from django.shortcuts import render, redirect
from .models import Bicicleta
from .forms import BicicletaForm

# Create your views here.
def listar_bicicletas(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, "Bicicleta/listar_bicicletas.html", {'bicicletas': bicicletas})

def agregar_bicicleta(request):
    if request.method == "POST":
        form = BicicletaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/listar_bicicletas")
    else:
        form = BicicletaForm()
        return render(request, "Bicicleta/agregar_bicicleta.html", {'form': form})

def borrar_bicicleta(request, bicicleta_id):
    # Recuperamos la instancia de la bicicleta y la borramos
    instancia = Bicicleta.objects.get(id=bicicleta_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_bicicletas')

def editar_bicicleta(request, bicicleta_id):
    # Recuperamos la instancia de la carrera
    instancia = Bicicleta.objects.get(id=bicicleta_id)

    # Creamos el formulario con los datos de la instancia
    form = BicicletaForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = BicicletaForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()
            return redirect('listar_bicicletas')

    # Si llegamos al final renderizamos el formulario
    return render(request, "Bicicleta/editar_bicicleta.html", {'form': form})
