from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'private/dashboard.html'),
<<<<<<< HEAD
    path('private/usuarios/', views.listar_usuarios, name='listar_usuarios'),

=======
    path('listar_usuarios/', views.listar_usuarios, name = 'listar_usuarios'),
>>>>>>> 42456cd6253a57af90d9b0b8663fe9c39b75d9de
]