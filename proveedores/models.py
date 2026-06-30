from django.db import models

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    representante = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_empresa