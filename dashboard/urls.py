from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'private/dashboard.html'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'), 
    path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
]