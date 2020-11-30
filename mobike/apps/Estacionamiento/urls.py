from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [
    # listar las carreras de la bd
    path('listar_estacionamientos', views.listar_estacionamientos, name="listar_estacionamientos"),
    
    # agregar una carrera    
    path('agregar_estacionamiento', views.agregar_estacionamiento, name="agregar_estacionamiento"),

    # ver detalle de un estacionamiento
    path('ver_estacionamiento/<int:estacionamiento_id>', views.ver_estacionamiento ,name="ver_estacionamiento"),

    # editar una carrera
    path('editar_estacionamiento/<int:estacionamiento_id>', views.editar_estacionamiento, name="editar_estacionamiento"),

    # borrar una carrera
    path('borrar_bicileta/<int:estacionamiento_id>', login_required(views.borrar_estacionamiento), name="borrar_estacionamiento"),
]
