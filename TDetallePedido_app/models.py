from django.db import models
from TPedidos_app.models import TPedido
from TProductos_app.models import TProducto
# Create your models here.

class TDetallePedido(models.Model):
    detalleid = models.IntegerField(primary_key=True)
    pedidoid = models.ForeignKey(TPedido,on_delete=models.CASCADE)
    productoid = models.ForeignKey(TProducto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    preciounitario = models.DecimalField(max_digits=6,decimal_places=2)
    subtotal = models.DecimalField(max_digits=7,decimal_places=2)
    notas = models.TextField()

    def __str__(self):
        return f"Pedido: {self.pedidoid} - Detalle: {self.detalleid} - Producto: {self.productoid}"