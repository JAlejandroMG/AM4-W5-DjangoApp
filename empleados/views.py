from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from empleados.models import Empleado
from empleados.serializer import EmpleadoSerializer, EmpleadoDetailSerializer


class EmpleadosViewSet(ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    # permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return EmpleadoDetailSerializer
        return EmpleadoSerializer
