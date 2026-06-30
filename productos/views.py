from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto
from proveedores.models import Proveedor

# ---------------- LISTAR PRODUCTOS ----------------
def listar_productos(request):
    productos_db = Producto.objects.all().order_by('-id')
    return render(request, 'productos/listar_productos.html', {'productos': productos_db})


# ---------------- CREAR PRODUCTO ----------------
def crear_productos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio_compra = request.POST.get('precio_compra')
        precio_venta = request.POST.get('precio_venta')
        stock = request.POST.get('stock')
        stock_minimo = request.POST.get('stock_minimo')
        id_proveedor = request.POST.get('id_proveedor')

        proveedor_instancia = None
        if id_proveedor:
            proveedor_instancia = get_object_or_404(Proveedor, id=id_proveedor)

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio_compra=precio_compra,
            precio_venta=precio_venta,
            stock=stock,
            stock_minimo=stock_minimo,
            proveedor=proveedor_instancia
        )
        messages.success(request, 'Producto guardado exitosamente.')
        return redirect('listar_productos')

    proveedores = Proveedor.objects.all()
    return render(request, 'productos/crear_producto.html', {'proveedores': proveedores})


# ---------------- EDITAR PRODUCTO ----------------
def editar_productos(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio_compra = request.POST.get('precio_compra')
        producto.precio_venta = request.POST.get('precio_venta')
        producto.stock = request.POST.get('stock')
        producto.stock_minimo = request.POST.get('stock_minimo')

        id_proveedor = request.POST.get('id_proveedor')
        if id_proveedor:
            producto.proveedor = get_object_or_404(Proveedor, id=id_proveedor)
        else:
            producto.proveedor = None

        producto.save()
        messages.success(request, 'Producto actualizado correctamente.')
        return redirect('listar_productos')

    proveedores = Proveedor.objects.all()
    return render(request, 'productos/editar_producto.html', {
        'producto': producto,
        'proveedores': proveedores
    })


# ---------------- ELIMINAR PRODUCTO ----------------
def eliminar_productos(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, 'Producto eliminado del inventario.')
    return redirect('listar_productos')