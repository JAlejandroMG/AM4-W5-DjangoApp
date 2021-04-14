from rest_framework.viewsets import ModelViewSet

from permisos.models import Permiso
from permisos.serializer import PermisoSerializer, PermisoDetailSerializer


class PermisosViewSet(ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PermisoDetailSerializer
        return PermisoSerializer
