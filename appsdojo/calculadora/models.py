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
