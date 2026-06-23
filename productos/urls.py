from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name = 'listar_productos'),
    path('crear_producto', views.crear_productos, name = 'crear_producto'),
    path('eliminar/<int:id>/', views.eliminar_productos, name='eliminar_productos'),
    path('editar/<int:id>/', views.editar_productos, name='editar_productos'),
]