from django.urls import path, include
from . import views

urlpatterns = [
    # listar las carreras de la bd
    path('listar_estacionamientos', views.listar_estacionamientos, name="listar_estacionamientos"),
    
    # agregar una carrera    
    path('agregar_estacionamiento', views.agregar_estacionamiento, name="agregar_estacionamiento"),

    # editar una carrera
    path('editar_estacionamiento/<int:estacionamiento_id>', views.editar_estacionamiento, name="editar_estacionamiento"),

    # borrar una carrera
    path('borrar_bicileta/<int:estacionamiento_id>', views.borrar_estacionamiento, name="borrar_estacionamiento"),
]
