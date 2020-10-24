from django.urls import path, include
from . import views

urlpatterns = [
    # listar las carreras de la bd
    path('listar_bicicletas', views.listar_bicicletas, name="listar_bicicletas"),
    
    # agregar una carrera    
    path('agregar_bicicleta', views.agregar_bicicleta, name="agregar_bicicleta"),

    # editar una carrera
    path('editar_bicicleta/<int:bicicleta_id>', views.editar_bicicleta ,name="editar_bicicleta"),

    # borrar una carrera
    path('borrar_bicileta/<int:bicicleta_id>', views.borrar_bicicleta, name="borrar_bicicleta"),

]
