from datetime import datetime

from django.db import models


class Receita(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.TextField()
    preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = 'Receitas'

    def __str__(self) -> str:
        return self.nome
