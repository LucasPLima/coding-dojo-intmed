
from calculadora.models import Calculadora
from rest_framework import filters, viewsets

from ..serializers import CalculadoraSerializer


class CalculadoraViewSet(viewsets.ModelViewSet):
    queryset = Calculadora.objects.all()
    serializer_class = CalculadoraSerializer
    
