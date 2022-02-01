
from rest_framework import serializers

from ..models import Calculadora


class CalculadoraSerializer(serializers.ModelSerializer):

    class Meta:
        model=Calculadora
        fields = ('id', 'nome', 'descricao', 'expressao')
