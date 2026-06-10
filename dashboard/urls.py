from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'private/dashboard.html'),
    path('private/usuarios/', views.listar_usuarios, name='listar_usuarios'),

]