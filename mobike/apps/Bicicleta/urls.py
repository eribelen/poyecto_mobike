from django.urls import path, include
from django.contrib.auth.views import login_required
from . import views

urlpatterns = [
    # listar las carreras de la bd
    path('listar_bicicletas', views.listar_bicicletas, name="listar_bicicletas"),
    
    # agregar una carrera    
    path('agregar_bicicleta', views.agregar_bicicleta, name="agregar_bicicleta"),

    # ver detalle de una bicicleta
    path('ver_bicicleta/<int:bicicleta_id>', views.ver_bicicleta ,name="ver_bicicleta"),

    # editar una carrera
    path('editar_bicicleta/<int:bicicleta_id>', views.editar_bicicleta ,name="editar_bicicleta"),

    # borrar una carrera
    path('borrar_bicileta/<int:bicicleta_id>', login_required(views.borrar_bicicleta), name="borrar_bicicleta"),

]
