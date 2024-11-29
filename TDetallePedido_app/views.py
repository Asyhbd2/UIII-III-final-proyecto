from django.shortcuts import render, redirect
from .models import TDetallePedido
from TPedidos_app.models import TPedido
from TProductos_app.models import TProducto

# Vista inicial para gestionar los detalles del pedido
def inicio_vistaDetallesPedido(request):
    losdetalles = TDetallePedido.objects.all()
    return render(request, "gestionarDetalle.html", {"misdetalles": losdetalles})

# Seleccionar un detalle de pedido para editar
def seleccionarDetallePedido(request, detalleid):
    detalle = TDetallePedido.objects.get(detalleid=detalleid)
    return render(request, "editarDetalle.html", {"losdetalles": detalle})

# Registrar un nuevo detalle de pedido
def registrarDetallePedido(request):
    detalleid = request.POST["numid"]
    pedidoid = TPedido.objects.get(pedidoid=request.POST["pedidoid"])  # Obtenemos el pedido asociado
    productoid = TProducto.objects.get(productoid=request.POST["productoid"])  # Obtenemos el producto asociado
    cantidad = request.POST["intcantidad"]
    preciounitario = request.POST["decimalpreciounitario"]
    subtotal = request.POST["decimalsubtotal"]
    notas = request.POST["txtnotas"]

    guardarDetalle = TDetallePedido.objects.create(
        detalleid=detalleid,
        pedidoid=pedidoid,
        productoid=productoid,
        cantidad=cantidad,
        preciounitario=preciounitario,
        subtotal=subtotal,
        notas=notas,
    )
    return redirect("inicio_vistaDetallesPedido")

# Editar un detalle de pedido existente
def editarDetallePedido(request):
    detalleid = request.POST["numid"]
    pedidoid = TPedido.objects.get(pedidoid=request.POST["pedidoid"])  # Obtenemos el pedido asociado
    productoid = TProducto.objects.get(productoid=request.POST["productoid"])  # Obtenemos el producto asociado
    cantidad = request.POST["intcantidad"]
    preciounitario = request.POST["decimalpreciounitario"]
    subtotal = request.POST["decimalsubtotal"]
    notas = request.POST["txtnotas"]

    detalle = TDetallePedido.objects.get(detalleid=detalleid)
    detalle.pedidoid = pedidoid
    detalle.productoid = productoid
    detalle.cantidad = cantidad
    detalle.preciounitario = preciounitario
    detalle.subtotal = subtotal
    detalle.notas = notas

    detalle.save()
    return redirect("inicio_vistaDetallesPedido")

# Eliminar un detalle de pedido
def borrarDetallePedido(request, detalleid):
    detalle = TDetallePedido.objects.get(detalleid=detalleid)
    detalle.delete()
    return redirect("inicio_vistaDetallesPedido")