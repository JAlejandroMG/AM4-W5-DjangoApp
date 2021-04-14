from rest_framework.serializers import ModelSerializer

from catalogo_permisos.serializer import CatalogoPermisoSerializer
from empleados.serializer import EmpleadoSerializer
from permisos.models import Permiso


class PermisoSerializer(ModelSerializer):
    class Meta:
        model = Permiso
        fields = ('id', 'active', 'time_span_days', 'catalogo_permisos', 'empleados')


class PermisoDetailSerializer(ModelSerializer):
    empleados = EmpleadoSerializer()
    catalogo_permisos = CatalogoPermisoSerializer()

    class Meta:
        model = Permiso
        fields = ('id', 'active', 'time_span_days', 'catalogo_permisos', 'empleados')
