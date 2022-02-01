from django.db import models


# Create your models here.
class Calculadora(models.Model):
    nome = models.CharField(
        null=False, max_length=255, unique=True, db_column="nm_calculadora"
    )
    
    descricao = models.TextField(
        blank=True, null=True, db_column='ds_calculadora'
    )

    expressao = models.TextField(blank=True, db_column='ds_expressao')

    def __str__(self) -> str:
        return f'{self.nome} - {self.descricao}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Calculadora'

class VariavelCalculadora(models.Model):
    nome = models.CharField(null=False, max_length=255, db_column='nm_variavel')
    identificador = models.CharField(
        null=False, max_length=50, db_column='nm_identificador'
    )
    unidade = models.CharField(
        null=True, blank=True, max_length=10, db_column='nm_unidade'
    )
    
    calculadora = models.ForeignKey(
        Calculadora,
        on_delete=models.CASCADE,
        related_name='variaveis',
        db_column='cd_calculadora',
    )

    class Meta:
        verbose_name = 'Variavel'

    def __str__(self) -> str:
        return f'{self.identificador}: {self.nome}({self.unidade})'
