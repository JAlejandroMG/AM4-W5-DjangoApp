from rest_framework.serializers import ModelSerializer

from empleados.models import Empleado
from puestos.serializer import PuestoSerializer


class EmpleadoSerializer(ModelSerializer):

    class Meta:
        model = Empleado
        fields = ('id', 'nombre', 'apellido', 'telefono', 'email', 'puestos')


class EmpleadoDetailSerializer(ModelSerializer):
    puestos = PuestoSerializer()

    class Meta:
        model = Empleado
        fields = ('nombre', 'apellido', 'telefono', 'email', 'puestos')
