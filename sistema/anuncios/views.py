from .models import Anuncio
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .forms import AnuncioForm
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListarAnuncios(LoginRequiredMixin,ListView):
    model = Anuncio
    context_object_name = 'veiculos'
    template_name = 'anuncios/listar_anuncios.html'

class CadastrarAnuncio(LoginRequiredMixin,CreateView):
    model = Anuncio
    form_class = AnuncioForm
    context_object_name = 'anuncios'
    # template_name = 'veiculos/cadastrar.html'
    # success_url = reverse_lazy('listar-veiculos') 

class EditarAnuncio(LoginRequiredMixin,UpdateView):
    model = Anuncio
    form_class = Anuncio
    context_object_name = 'anuncios'
    # template_name = 'veiculos/editar.html'
    # success_url = reverse_lazy('listar-veiculos') 

class ExcluirAnuncio(LoginRequiredMixin,DeleteView):
    model = Anuncio
    context_object_name = 'anuncios'
    # template_name = 'alert.html'
    # success_url = reverse_lazy('listar-veiculos') 
