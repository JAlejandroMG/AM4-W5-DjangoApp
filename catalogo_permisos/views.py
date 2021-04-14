from rest_framework.viewsets import ModelViewSet

from catalogo_permisos.models import CatalogoPermiso
from catalogo_permisos.serializer import CatalogoPermisoSerializer


class CatalogoPermisosViewSet(ModelViewSet):
    queryset = CatalogoPermiso.objects.all()
    serializer_class = CatalogoPermisoSerializer
