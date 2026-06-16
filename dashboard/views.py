<<<<<<< Updated upstream
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
=======
from urllib import request

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
>>>>>>> Stashed changes

# --- Vista del Dashboard ---
def dashboard(request):
    return render(request, 'dashboard.html')

<<<<<<< Updated upstream
=======

# --- Vista para Listar Usuarios ---
>>>>>>> Stashed changes
def listar_usuarios(request):
    usuarios = User.objects.all()
    contexto = {
        'usuarios': usuarios
    }
    return render(request, 'private/listar_usuarios.html', contexto)

<<<<<<< Updated upstream
def crear_usuario(request):
    if request.method=='POST':
        username_req=request.POST.get('username')
        email_req=request.POST.get('email')
        password_req=request.POST.get('password')
        
        if not username_req or not email_req or not password_req:
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'private/crear_usuarios.html')
            
        try:
            if User.objects.filter(username=username_req).exists():
                messages.error(request, f'El nombre de usuario "{username_req}" ya está en uso.')
                return render(request, 'private/crear_usuarios.html')
                
            nuevo_usuario = User.objects.create_user(
                username=username_req,
                email=email_req,
                password=password_req
            )
            nuevo_usuario.save()
            
            messages.success(request, f'El usuario {username_req} ha sido creado con éxito.')
            return redirect('listar_usuarios')
            
        except Exception as e:
            messages.error(request, f'Ocurrió un error al registrar el usuario: {str(e)}')
            return render(request, 'private/crear_usuarios.html')
            
    return render(request, 'private/crear_usuarios.html')
def eliminar_usuario(request, usuario_id):
    usuario = User.objects.get(id=usuario_id)
    usuario.delete()
    
    messages.success(request, 'El usuario ha sido eliminado correctamente del sistema.')
    return redirect('listar_usuarios')
=======

# --- Vista para Crear Usuarios ---
def crear_usuarios(request):
    if request.method == 'POST':  # Corregido: 'POST' debe ir en mayúsculas
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")  # Corregido: de POSAT a POST

        # Validación 1: ¿El usuario ya existe?
        if User.objects.filter(username=username).exists():  # Corregido: fiñter -> filter
            messages.error(request, "El usuario ya existe.")
            return render(request, 'private/crear_usuarios.html')

        # Validación 2: ¿El correo ya existe?
        if User.objects.filter(email=email).exists():  # Corregido: faltaba el punto antes de exists()
            messages.error(request, "El correo ya existe.")
            return render(request, 'private/crear_usuarios.html')

        # Si todo está bien, creamos el usuario de forma segura
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "¡Usuario creado con éxito!")
        
        # Es buena práctica redireccionar tras un POST exitoso para evitar reenvíos de formulario
        return redirect('listar_usuarios') 

    # Si la petición es GET (cuando entran por primera vez a la página)
    return render(request, 'private/crear_usuarios.html')

# Código del final corregido en su sintaxis:
User.objects.create_user(
    username="username",
    email="email",
    password="password"
)

messages.success(request, "usuario creado con exito")
return render(request, "private/lista_usuarios.html")
return render(request, "private/")
>>>>>>> Stashed changes
