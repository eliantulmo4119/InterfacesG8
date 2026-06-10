from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required  # Importamos el protector de rutas

# 1. Vista de la página de inicio pública (Landing Page de la Vulca)
def vulca(request):
    return render(request, 'index.html')

# 2. Vista pública de Login (Carga el formulario)
def login(request):
    return render(request, 'login.html')

# Vista para mostrar nuestra historia.
def nosotros(request):
    return render(request, 'nosotros.html')

def control_neu(request):
    return render(request, 'control_neu.html')

def gestion_tubos(request):
    return render(request, 'gestion_tubos.html')

def contacto(request):
    return render(request, 'contacto.html')


# 3. VISTA DEL DASHBOARD PRIVADO (Corregido el nombre)
@login_required  # Si intentan entrar sin loguearse, Django los mandará al login
def dashboard_view(request):
    # Aquí es donde realmente se carga tu panel de control privado
    return render(request, 'private/dashboard.html')


# 4. Procesamiento del Formulario de Login (POST)
def login_view(request):
    mensaje = ''
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            # Redirige al alias 'dashboard' que ahora apuntará a la función correcta
            return redirect('dashboard')  
        else:
            # Si las credenciales fallan
            mensaje = 'Usuario o contraseña incorrectos'
            
    return render(request, 'login.html', {'mensaje': mensaje})