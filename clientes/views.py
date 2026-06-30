from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente

# ---------------- LISTAR CLIENTES ----------------
def listar_clientes(request):
    clientes = Cliente.objects.all().order_by('-id')
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})


# ---------------- CREAR CLIENTE ----------------
def crear_cliente(request):
    if request.method == 'POST':
        cedula_ruc = request.POST.get('cedula_ruc')
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')

        # Validación de campos obligatorios
        if not cedula_ruc or not nombre:
            messages.error(request, 'La cédula/RUC y el nombre son obligatorios.')
            return render(request, 'clientes/crear_cliente.html')

        # Verificar si ya existe la cédula o RUC
        if Cliente.objects.filter(cedula_ruc=cedula_ruc).exists():
            messages.error(request, 'Un cliente con esta cédula o RUC ya está registrado.')
            return render(request, 'clientes/crear_cliente.html')

        # Guardar en la base de datos MySQL
        Cliente.objects.create(
            cedula_ruc=cedula_ruc,
            nombre=nombre,
            telefono=telefono,
            email=email,
            direccion=direccion
        )

        messages.success(request, 'Cliente registrado con éxito.')
        return redirect('listar_clientes')

    return render(request, 'clientes/crear_cliente.html')


# ---------------- EDITAR CLIENTE ----------------
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == 'POST':
        cedula_ruc = request.POST.get('cedula_ruc')
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')

        # Validar duplicados de cédula excluyendo al cliente actual
        if Cliente.objects.filter(cedula_ruc=cedula_ruc).exclude(id=id).exists():
            messages.error(request, 'Esta cédula o RUC ya pertenece a otro cliente.')
            return render(request, 'clientes/editar_cliente.html', {'cliente': cliente})

        # Actualizar datos
        cliente.cedula_ruc = cedula_ruc
        cliente.nombre = nombre
        cliente.telefono = telefono
        cliente.email = email
        cliente.direccion = direccion
        cliente.save()

        messages.success(request, 'Los datos del cliente se actualizaron con éxito.')
        return redirect('listar_clientes')

    return render(request, 'clientes/editar_cliente.html', {'cliente': cliente})


# ---------------- ELIMINAR CLIENTE ----------------
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    try:
        nombre_cliente = cliente.nombre
        cliente.delete()
        messages.success(request, f'Cliente "{nombre_cliente}" eliminado correctamente.')
    except Exception as e:
        messages.error(request, f'Error al eliminar el cliente: {str(e)}')
        
    return redirect('listar_clientes')