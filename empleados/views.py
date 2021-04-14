from rest_framework.viewsets import ModelViewSet

from empleados.models import Empleado
from empleados.serializer import EmpleadoSerializer


class EmpleadosViewSet(ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
