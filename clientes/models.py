from django.db import models

class Cliente(models.Model):
    cedula_ruc = models.CharField(max_length=13, unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clientes' # Forzamos el nombre exacto de tu tabla MySQL

    def __str__(self):
        return self.nombre