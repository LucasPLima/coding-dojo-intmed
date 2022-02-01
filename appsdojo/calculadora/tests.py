from django.test import TestCase

from appsdojo.calculadora.models import Calculadora
from appsdojo.calculadora.serializers import calculadora

# Create your tests here.
class CalculadoraTest(TestCase):
    def setUp(self):
        Calculadora.objects.create(nome="Calculadora Teste", descricao="Teste", expressao="peso + 3")

    def test_criacao_calculadora(self):
        calculadora = Calculadora.objects.get(nome="Calculadora Teste")
        self.assertEqual()