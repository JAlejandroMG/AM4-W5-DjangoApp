from django.db import models

from catalogo_permisos.models import CatalogoPermiso
from empleados.models import Empleado


class Permiso(models.Model):
    active = models.BooleanField(default=True)
    time_span_days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    catalogo_permisos = models.ForeignKey(
        CatalogoPermiso,
        related_name='permisos',
        on_delete=models.SET_NULL,
        null=True
    )
    empleados = models.ForeignKey(
        Empleado,
        related_name='permisos',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.nombre
