

from calculadora.models import Calculadora, VariavelCalculadora
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from ..serializers import CalculadoraSerializer, VariavelCalculadoraSerializer


class CalculadoraViewSet(viewsets.ModelViewSet):
    queryset = Calculadora.objects.filter()
    serializer_class = CalculadoraSerializer
    
class VariavelCalculadoraViewSet(viewsets.ViewSet):
    
    def list(self, request, calculadora_pk=None):
        queryset = VariavelCalculadora.objects.filter(calculadora=calculadora_pk)
        serializer = VariavelCalculadoraSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request,pk=None, calculadora_pk=None):
        queryset = VariavelCalculadora.objects.filter(pk=pk, calculadora=calculadora_pk)
        variavel = get_object_or_404(queryset, pk=pk)
        serializer = VariavelCalculadoraSerializer(variavel)
        return Response(serializer.data)

    def create(self, request, calculadora_pk=None):
        serializer = VariavelCalculadoraSerializer(data=request.data, context={'calculadora_pk':calculadora_pk})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None, calculadora_pk=None):
        queryset = VariavelCalculadora.objects.filter()
        variavel = get_object_or_404(queryset, pk=pk)
        variavel.delete()
        return Response(status=status.HTTP_200_OK)
