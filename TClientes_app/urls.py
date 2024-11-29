from django.urls import path
from TClientes_app import views

urlpatterns = [
    path("cliente",views.inicio_vistaCliente,name="inicio_vistaCliente"),
    path("registrarCliente/",views.registrarCliente,name="registrarCliente"),
    path("seleccionarCliente/<clienteid>",views.seleccionarCliente,name="seleccionarCliente"),
    path("editarCliente/",views.editarCliente,name="editarCliente"),
    path("borrarCliente/<clienteid>",views.borrarCliente,name="borrarCliente")
]
