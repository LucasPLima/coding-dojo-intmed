
from pyexpat import model
from rest_framework import serializers

from ..models import Calculadora, VariavelCalculadora


class VariavelCalculadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model=VariavelCalculadora
        fields = (
            'id',
            'nome',
            'identificador',
            'unidade',
        )
    
    def create(self, validated_data):
        variavel_new= VariavelCalculadora()
        variavel_new.nome=validated_data.get('nome', None)
        variavel_new.identificador=validated_data.get('identificador', None)
        variavel_new.unidade=validated_data.get('unidade', None)
        
        calculadora = Calculadora.objects.get(pk=self.context.get('calculadora_pk',None))
        variavel_new.calculadora= calculadora
        variavel_new.save()
        return variavel_new


class CalculadoraSerializer(serializers.ModelSerializer):
    variaveis = VariavelCalculadoraSerializer(many=True, read_only=True)
    class Meta:
        model=Calculadora
        fields = ('id', 'nome', 'descricao', 'expressao', 'variaveis')
