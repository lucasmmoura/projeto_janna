from django.db import models

# Create your models here.


class Campeao(models.Model):
    nome = models.CharField(
        max_length = 100,
        verbose_name = 'Nome do campeão',
    )

    funcao = models.CharField(
        verbose_name = 'Função do campeão',
        max_length = 100
    )

    descricao = models.TextField(
        verbose_name = 'Descrição do campeão'
    )

    class Meta:
        verbose_name = 'Campeão',
        verbose_name_plural = 'Campeões'

    def __str__(self):
        return self.nome