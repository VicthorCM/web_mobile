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

    @property
    def veiculo_novo(self):
        return self.ano == datetime.now().year
   
    def anos_de_uso(self):
        return datetime.now().year - self.ano
    
    class Meta:
        ordering = ('-id',)