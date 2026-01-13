from django.db import models
from django.utils.text import slugify
# Create your models here.


class Campeao(models.Model):
    nome = models.CharField(
        max_length = 100,
        verbose_name = 'Nome do campeão',
    )

    slug = models.SlugField(
        unique = True,
        blank = True
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome