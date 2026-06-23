from django.contrib import messages

from django.shortcuts import redirect, render
from .models import Producto

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/listar_productos.html", 
                  {'productos' : productos})

def crear_productos(request):
    if request.method == "POST":
        nombre_producto = request.POST.get("nombreProducto") #PONER NOMBRE DEL FORM
        precio_producto = request.POST.get("precioProducto")
        stock_producto = request.POST.get("stockProducto")
        estado_producto = request.POST.get("estadoProducto")

        Producto.objects.create(
            nombre_producto = nombre_producto,
            precio_producto = precio_producto,
            stock_producto = stock_producto,
            estado_producto = estado_producto
        )
        return redirect('listar_productos')
    return render(request, 'productos/crear_productos.html')

def eliminar_productos(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    messages.success(request, "Producto Eliminado.")
    return redirect("listar_productos")

def editar_productos(request, id):
    producto = Producto.objects.get(id = id)

    if request.method == "POST":
        producto.nombre_producto = request.POST.get("nombreProducto")
        producto.precio_producto = request.POST.get("precioProducto")
        producto.stock_producto = request.POST.get("stockProducto")
        producto.estado_producto = request.POST.get("estadoProducto")

        producto.save()
        messages.success(request, "Producto Actualizado")
        return redirect("listar_productos")
    return render(request, "productos/editar_productos.html", {"producto" : producto})