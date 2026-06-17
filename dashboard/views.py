from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages


# ---------------- DASHBOARD ----------------
def dashboard(request):
    return render(request, 'dashboard.html')


# ---------------- LISTAR USUARIOS ----------------
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'private/listar_usuarios.html', {'usuarios': usuarios})


# ---------------- CREAR USUARIO ----------------
def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'private/crear_usuarios.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe.')
            return render(request, 'private/crear_usuarios.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya existe.')
            return render(request, 'private/crear_usuarios.html')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, 'Usuario creado con éxito.')
        return redirect('listar_usuarios')

    return render(request, 'private/crear_usuarios.html')


# ---------------- ELIMINAR USUARIO ----------------
def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)

    try:
        nombre = usuario.username
        usuario.delete()

        messages.success(request, f'Usuario "{nombre}" eliminado correctamente.')

    except Exception as e:
        messages.error(request, f'Error al eliminar: {str(e)}')

    return redirect('listar_usuarios')

def editar_usuario(request, id): #Metodo de editar
    usuario = User.objects.get(id = id)
    if request.method == "POST":
        username = request.POST.get("")
        email = request.POST.get("")
        password = request.POST.get("")
        #VERIFIQUE SI EXISTE EL USERNAME
        if User.objects.filter(username = username).exclude(id = id).exists():
            messages.error(request, "El usuario ya está registrado.")
            return render(request, "private/editar_usuario.html", {"usuario":usuario})
        #VERIFIQUE SI EXISTE EL EMAIL
        if User.objects.filter(email = email).exclude(id = id).exists():
            messages.error(request, "El correo ya existe")
            return render(request, "private/editar_usuario.html", {"usuario":usuario})
        #ACUTALIZAR DATOS
        usuario.username = username
        usuario.email = email
        usuario.password = password

        usuario.save()
        messages.success(request, "El registro se actualizó con éxito")
        return redirect("listar_usuarios")
    contexto = {
        "usuario":usuario
    }