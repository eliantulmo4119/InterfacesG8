from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Proveedor


# LISTAR
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "proveedores/listar_proveedores.html", {
        "proveedores": proveedores
    })


# CREAR
def crear_proveedor(request):

    if request.method == "POST":
        Proveedor.objects.create(
            nombre_empresa=request.POST['nombre_empresa'],
            representante=request.POST['representante'],
            telefono=request.POST['telefono'],
            correo=request.POST['correo'],
            direccion=request.POST['direccion']
        )

        messages.success(request, "Proveedor creado correctamente")
        return redirect("listar_proveedores")

    return render(request, "proveedores/crear_proveedor.html")


# EDITAR
def editar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)

    if request.method == "POST":
        proveedor.nombre_empresa = request.POST['nombre_empresa']
        proveedor.representante = request.POST['representante']
        proveedor.telefono = request.POST['telefono']
        proveedor.correo = request.POST['correo']
        proveedor.direccion = request.POST['direccion']
        proveedor.save()

        messages.success(request, "Proveedor actualizado")
        return redirect("listar_proveedores")

    return render(request, "proveedores/editar_proveedor.html", {
        "proveedor": proveedor
    })


# ELIMINAR
def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    messages.success(request, "Proveedor eliminado")
    return redirect("listar_proveedores")