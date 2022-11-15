from django.db import models
from django.contrib.auth.models import AbstractUser

class Pessoas(AbstractUser):
    cep = models.CharField(max_length=8, blank=True)
    rua = models.CharField(max_length=100, blank=True)
    numero = models.IntegerField(blank=True, null=True)