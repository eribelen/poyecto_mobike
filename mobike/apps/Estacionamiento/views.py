from django.shortcuts import render, redirect
from .models import Estacionamiento
from .forms import EstacionamientoForm

# Create your views here.
def listar_estacionamientos(request):
    estacionamientos = Estacionamiento.objects.all()
    return render(request, "Estacionamiento/listar_estacionamientos.html", {'estacionamientos': estacionamientos})

def ver_estacionamiento(request, estacionamiento_id):
    estacionamiento = Estacionamiento.objects.get(id=estacionamiento_id)
    return render(request, "Estacionamiento/ver_estacionamiento.html", {'estacionamiento': estacionamiento})

def agregar_estacionamiento(request):
    if request.method == "POST":
        form = EstacionamientoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("listar_estacionamientos")
    else:
        form = EstacionamientoForm()
        return render(request, "Estacionamiento/agregar_estacionamiento.html", {'form': form})

def borrar_estacionamiento(request, estacionamiento_id):
    # Recuperamos la instancia de la estacionamiento y la borramos
    instancia = Estacionamiento.objects.get(id=estacionamiento_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_estacionamientos')

def editar_estacionamiento(request, estacionamiento_id):
    # Recuperamos la instancia de la carrera
    instancia = Estacionamiento.objects.get(id=estacionamiento_id)

    # Creamos el formulario con los datos de la instancia
    form = EstacionamientoForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = EstacionamientoForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()
            return redirect('listar_estacionamientos')

    # Si llegamos al final renderizamos el formulario
    return render(request, "Estacionamiento/editar_estacionamiento.html", {'form': form})
