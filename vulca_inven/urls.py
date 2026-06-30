from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('', include('vulca.urls')), 
    path('productos/', include('productos.urls')),
    path('proveedores/', include('proveedores.urls')),
    
    # 🚨 NUEVA APLICACIÓN: GESTIÓN DE CLIENTES 🚨
    path('clientes/', include('clientes.urls')),
]