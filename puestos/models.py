from django.db import models

class Puesto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
