from datetime import datetime

from django.db import models
from usuarios.models import Usuarios

from stdimage.models import StdImageField


class Receita(models.Model):
    pessoa = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    ingredientes = models.TextField()
    descricao = models.CharField(max_length=80)
    preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    foto = StdImageField(upload_to='fotos/%d/%m/%Y',variations={'thumb': (365, 280)} ,blank=True)
    publicada = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Receitas'

    def __str__(self) -> str:
        return self.nome
