from django.shortcuts import render,redirect
from .models import TCliente
# Create your views here.

def inicio_vistaCliente(request):
    losclientes=TCliente.objects.all()
    return render(request,"gestionarCliente.html",{"misclientes":losclientes})

def registrarCliente(request):
    clienteid=request.POST["numid"]
    nombre=request.POST["txtnombre"]
    correo=request.POST["txtcorreo"]
    telefono=request.POST["txttelefono"]
    direccion=request.POST["txtdireccion"]
    fecharegistro=request.POST["datefecha"]

    guardarCliente=TCliente.objects.create(
        clienteid=clienteid,nombre=nombre,correo=correo,telefono=telefono,direccion=direccion,fecharegistro=fecharegistro
    ) # GUARDA EL REGISTRO

    return redirect("inicio_vistaCliente")

def seleccionarCliente(request,clienteid):
    cliente=TCliente.objects.get(clienteid=clienteid)
    return render(request,"editarCliente.html",{"misclientes":cliente})

def editarCliente(request):
    clienteid=request.POST["numid"]
    nombre=request.POST["txtnombre"]
    correo=request.POST["txtcorreo"]
    telefono=request.POST["txttelefono"]
    direccion=request.POST["txtdireccion"]
    fecharegistro=request.POST["datefecha"]

    Cliente=TCliente.objects.get(clienteid=clienteid)
    Cliente.clienteid=clienteid
    Cliente.nombre=nombre
    Cliente.correo=correo
    Cliente.telefono=telefono
    Cliente.direccion=direccion
    Cliente.fecharegistro=fecharegistro
    Cliente.save() # GUARDA REGISTRO ACTUAL
    return redirect("inicio_vistaCliente")

def borrarCliente(request,clienteid):
    cliente=TCliente.objects.get(clienteid=clienteid)
    cliente.delete() # BORRA EL REGISTRO

    return redirect("inicio_vistaCliente")