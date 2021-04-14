from rest_framework.serializers import ModelSerializer

from catalogo_permisos.models import CatalogoPermiso


class CatalogoPermisoSerializer(ModelSerializer):
    class Meta:
        model = CatalogoPermiso
        fields = ('id', 'nombre', 'descripcion')

