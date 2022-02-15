from appsdojo.calculadora.serializers import calculadora
from calculadora.models import Calculadora
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

        

