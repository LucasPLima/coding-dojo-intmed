from appsdojo.calculadora.serializers import calculadora
from calculadora.models import Calculadora, VariavelCalculadora
from django.db.utils import IntegrityError
from django.test import TestCase

# Fazer o teste do CRUD da calculadora

# Verificar nome duplicado
# Fazer teste do CRUD da variável
# Validação de nome duplicado na mesma calculadora

# Create your tests here.
class CalculadoraTest(TestCase):
    def setUp(self):
        Calculadora.objects.create(nome="Calculadora Teste", descricao="Teste", expressao="peso + 3")
        Calculadora.objects.create(nome="Calculadora Teste 2", descricao="Teste", expressao="peso + 3")

    def test_criacao_calculadora(self):
        calculadora = Calculadora.objects.filter(nome="Calculadora Teste")
        self.assertEqual(calculadora.exists(), True)

    def test_atualiza_calculadora(self):
        calculadora = Calculadora.objects.get(nome="Calculadora Teste")
        calculadora.nome = "Novo nome atualizado"
        calculadora.save()

        self.assertEqual(Calculadora.objects.filter(nome="Novo nome atualizado").exists(), True)
        self.assertEqual(Calculadora.objects.filter(nome="Calculadora Teste").exists(), False)

    def test_atualiza_calculadora_nome_duplicado(self):
        calculadora = Calculadora.objects.get(nome="Calculadora Teste")
        calculadora.nome = "Calculadora Teste 2"
        
        # Espera um erro de integridade
        self.assertRaises(IntegrityError, calculadora.save)
    
    def test_deletar_calculadora(self):
        calculadora = Calculadora.objects.get(nome="Calculadora Teste")
        calculadora.delete()
        self.assertEqual(Calculadora.objects.filter(nome="Calculadora Teste").exists(), False)

    def test_criacao_calculadora_duplicada(self):
        self.assertRaises(IntegrityError,Calculadora.objects.create, 
         nome="Calculadora Teste" , descricao="Teste", expressao="peso + 3"
        )


class VariavelTest(TestCase):
    def setUp(self):
        self.calculadora = Calculadora.objects.create(nome="Calculadora Teste", descricao="Teste", expressao="peso + 3")
        self.variavel_1 = VariavelCalculadora.objects.create(nome="Variavel Teste", identificador="X", unidade="nulo", calculadora=self.calculadora)

    def test_criacao_variavel(self):
        self.assertEqual(VariavelCalculadora.objects.filter(nome="Variavel Teste").exists(), True)

    def test_atualiza_variavel(self):
        variavel = VariavelCalculadora.objects.get(nome="Variavel Teste", calculadora=self.calculadora)
        variavel.nome = "Marmelada"
        variavel.save()

        self.assertEqual(VariavelCalculadora.objects.filter(nome="Marmelada", calculadora=self.calculadora).exists(), True)

    def test_exclui_variavel(self):
        variavel= VariavelCalculadora.objects.filter(nome="Variavel Teste", calculadora=self.calculadora)
        variavel.delete()

        self.assertEqual(VariavelCalculadora.objects.filter(nome="Variavel Teste", calculadora=self.calculadora).exists(), False)

    def test_variavel_nome_duplicado_na_calculadora(self):
        self.assertRaises(IntegrityError, VariavelCalculadora.objects.create, nome="Variavel Teste", identificador="X", calculadora=self.calculadora)
