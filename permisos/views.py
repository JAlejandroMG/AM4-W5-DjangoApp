from rest_framework.viewsets import ModelViewSet

from permisos.models import Permiso
from permisos.serializer import PermisoSerializer


class PermisosViewSet(ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer
