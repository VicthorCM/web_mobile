from django.db import models
from datetime import datetime
from .consts import *

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS)
    foto = models.ImageField(blank=True, null= True, upload_to='veiculos/fotos')

    class Meta:
        ordering = ('-id',)