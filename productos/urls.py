from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('crear/', views.crear_productos, name='crear_producto'),
    path('editar/<int:id>/', views.editar_productos, name='editar_producto'),
    path('eliminar/<int:id>/', views.eliminar_productos, name='eliminar_producto'),
]