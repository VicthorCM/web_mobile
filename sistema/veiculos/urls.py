from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import *

urlpatterns= [
    path('', login_required(ListarVeiculos.as_view(),login_url='login'), name='listar-veiculos'),
    path('cadastrar/',login_required(CadastrarVeiculos.as_view(),login_url='login'), name='cadastrar-veiculos'),
    path('editar/<int:pk>/',login_required(EditarVeiculos.as_view(),login_url='login'), name='editar-veiculos'),
    path('excluir/<int:pk>/',login_required(ExcluirVeiculos.as_view(),login_url='login'), name='excluir-veiculos'),
    path('fotos/<str:arquivo>/',FotosVeiculo.as_view(), name='fotos-veiculo'),
    path( 'api/',ListarAPIVeiculos.as_view(),name='listar-veiculos-api')
]