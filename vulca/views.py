from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
def vulca(request):
    return render(request, 'index.html')
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
def hola(request):
    return render(request, 'dashboard.html')
def login_view(request):
    mensaje = ''
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            
            return redirect('dashboard')  
        else:
            # Si las credenciales fallan
            mensaje = 'Usuario o contraseña incorrectos'
            
    return render(request, 'login.html', {'mensaje': mensaje})