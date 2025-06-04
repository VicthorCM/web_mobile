from django.db import models
from veiculos.models import Veiculo
class Anuncio(models.Model):
    preco = models.DecimalField(max_digits=5,decimal_places=2) #mudar para int 
    veiculo = models.ForeignKey(Veiculo,on_delete=models.CASCADE,null=False)
    descricao = models.TextField(max_length=200,null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

