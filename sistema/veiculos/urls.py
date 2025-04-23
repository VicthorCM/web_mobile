from django.urls import path
from .views import *

urlpatterns= [
    path('', ListarVeiculos.as_view(), name='listar-veiculos')
]