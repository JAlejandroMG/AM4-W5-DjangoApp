from django.db import models

from puestos.models import Puesto


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    puestos = models.ForeignKey(
        Puesto,
        related_name='empleados',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
