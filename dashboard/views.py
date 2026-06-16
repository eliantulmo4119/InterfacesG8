from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages


def dashboard(request):
    return render(request, 'dashboard.html')


def listar_usuarios(request):
    usuarios = User.objects.all()

    contexto = {
        'usuarios': usuarios
    }

    return render(request, 'private/listar_usuarios.html', contexto)


def crear_usuario(request):
    if request.method == 'POST':
        username_req = request.POST.get('username')
        email_req = request.POST.get('email')
        password_req = request.POST.get('password')

        if not username_req or not email_req or not password_req:
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'private/crear_usuarios.html')

        try:
            if User.objects.filter(username=username_req).exists():
                messages.error(
                    request,
                    f'El nombre de usuario "{username_req}" ya está en uso.'
                )
                messages.error(request, f'El nombre de usuario "{username_req}" ya está en uso.')

                return render(request, 'private/crear_usuarios.html')

            nuevo_usuario = User.objects.create_user(
                username=username_req,
                email=email_req,
                password=password_req
            )

            nuevo_usuario.save()

            messages.success(
                request,
                f'El usuario "{username_req}" ha sido creado con éxito.'
            )

            return redirect('listar_usuarios')

        except Exception as e:
            messages.error(
                request,
                f'Ocurrió un error al registrar el usuario: {str(e)}'
            )

            return render(request, 'private/crear_usuarios.html')

    return render(request, 'private/crear_usuarios.html')


def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)

    try:
        nombre_usuario = usuario.username

        # Eliminación física
        usuario.delete()

        messages.success(
            request,
            f'El usuario "{nombre_usuario}" fue eliminado correctamente.'
        )

    except Exception as e:
        messages.error(
            request,
            f'Error al eliminar el usuario: {str(e)}'
        )

        return redirect('listar_usuarios')
    messages.error(request, f'Ocurrió un error al registrar el usuario: {str(e)}')
    return render(request, 'private/crear_usuarios.html')
            
    return render(request, 'private/crear_usuarios.html')

def eliminar_usuario(request, usuario_id):
    usuario = User.objects.get(id=usuario_id)
    usuario.delete()
    
    messages.success(request, 'El usuario ha sido eliminado correctamente del sistema.')
    return redirect('listar_usuarios')

