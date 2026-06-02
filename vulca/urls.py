from django.urls import path
from . import views

urlpatterns = [
    path('', views.vulca, name='index'), 
    path('login/', views.login, name='login'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('control_neu/', views.control_neu, name='control_neu'),
    path('gestion_tubos/', views.gestion_tubos, name='gestion_tubos'),
    path('contacto/', views.contacto, name='contacto'),
    path('hola.html', views.hola, name='hola'),  # Asegúrate de que esta URL corresponda a tu página de inicio
    path('login_view/', views.login_view, name='login_view'),  # URL para el proceso de login
]