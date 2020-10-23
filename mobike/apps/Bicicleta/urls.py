from django.urls import path, include
from . import views

urlpatterns = [
    # listar las carreras de la bd
    path('listarBicicletas', views.listar_bicicletas, name="listar_bicicletas"),
]
