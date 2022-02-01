from django.test import TestCase

from ..models import Calculadora

# Create your tests here.
class CalculadoraTest(TestCase):
    def setUp(self):
        Calculadora.objects.create(nome="Calculadora Teste", descricao="Teste", expressao="peso + 3")

    def test_criacao_calculadora(self):
        calculadora = Calculadora.objects.filter(nome="Calculadora Teste")
        self.assertEqual(calculadora.exists(), True)

