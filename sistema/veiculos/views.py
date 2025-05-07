from .models import Veiculo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import VeiculoForm
from django.urls import reverse_lazy

class ListarVeiculos(ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculos/listar.html'

class CadastrarVeiculos(CreateView):
    model = Veiculo
    form_class = VeiculoForm
    context_object_name = 'veiculos'
    template_name = 'veiculos/cadastrar.html'
    success_url = reverse_lazy('listar-veiculos') 

class EditarVeiculos(UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    context_object_name = 'veiculos'
    template_name = 'veiculos/cadastrar.html'
    success_url = reverse_lazy('listar-veiculos') 

class ExcluirVeiculos (DeleteView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'alert.html'
    success_url = reverse_lazy('listar-veiculos') 