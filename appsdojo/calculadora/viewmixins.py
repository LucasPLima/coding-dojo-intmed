from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response


class CalculadoraViewMixin(generics.GenericAPIView):
    @action(detail=True, methods=['post'], url_path='calcular')
    def calcular(self,request, pk):
        calculadora = self.get_object()
        variaveis = [
            variavel.identificador
            for variavel in calculadora.variaveis.all()
        ]
        expressao_eval = f"lambda {','.join(variaveis)}:{calculadora.expressao}"

        # TODO: Expressão deve ser salva no formato lambda já no serializer,
        # pra nesse ponto chamar apenas o eval
        funcaoLambda = eval(expressao_eval)
        valores = request.data.get("valores")
        resultado = funcaoLambda(*valores)
        return Response({'resultado': resultado})
