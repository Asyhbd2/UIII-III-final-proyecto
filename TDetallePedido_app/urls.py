from django.urls import path
from TDetallePedido_app import views

urlpatterns = [
    path("detallePedido", views.inicio_vistaDetallesPedido, name="inicio_vistaDetallesPedido"),
    path("registrarDetallePedido/", views.registrarDetallePedido, name="registrarDetallePedido"),
    path("editarDetallePedido/", views.editarDetallePedido, name="editarDetallePedido"),
    path("seleccionarDetallePedido/<detalleid>", views.seleccionarDetallePedido, name="seleccionarDetallePedido"),
    path("borrarDetallePedido/<detalleid>", views.borrarDetallePedido, name="borrarDetallePedido"),
]