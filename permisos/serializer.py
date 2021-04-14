from rest_framework.serializers import ModelSerializer

from permisos.models import Permiso


class PermisoSerializer(ModelSerializer):
    class Meta:
        model = Permiso
        fields = ('id', 'active', 'time_span_days', 'catalogo_permisos', 'empleados')
