from rest_framework.viewsets import ModelViewSet

from puestos.models import Puesto
from puestos.serializer import PuestoSerializer


class PuestosViewSet(ModelViewSet):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer
