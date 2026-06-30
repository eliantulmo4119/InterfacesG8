from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'), 
    path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('editar_usuario/<int:id>', views.editar_usuario, name = "editar_usuario"),
    path('reportes/estadisticas/', views.reporte_estadisticos, name='reportes_graficos'),
]