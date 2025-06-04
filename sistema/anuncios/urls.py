from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import *

urlpatterns= [
    path('',ListarAnuncios.as_view(), name='listar-anuncios'),
    path('cadastrar/',CadastrarAnuncio.as_view(), name='cadastrar-anuncio'),
    path('editar/<int:pk>/',EditarAnuncio.as_view(), name='editar-anuncio'),
    path('excluir/<int:pk>/',ExcluirAnuncio.as_view(), name='excluir-anuncio'),
]