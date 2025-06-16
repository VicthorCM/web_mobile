from .models import Veiculo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .forms import VeiculoForm
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView, DestroyAPIView
from .serializers import SerializadorVeiculo
from rest_framework. permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ListarVeiculos(LoginRequiredMixin,ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculos/listar.html'

class ListarAPIVeiculos(ListAPIView):
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()

class CadastrarVeiculos(LoginRequiredMixin,CreateView):
    model = Veiculo
    form_class = VeiculoForm
    context_object_name = 'veiculos'
    template_name = 'veiculos/cadastrar.html'
    success_url = reverse_lazy('listar-veiculos') 

class EditarVeiculos(LoginRequiredMixin,UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    context_object_name = 'veiculos'
    template_name = 'veiculos/editar.html'
    success_url = reverse_lazy('listar-veiculos') 

class ExcluirVeiculos (LoginRequiredMixin,DeleteView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'alert.html'
    success_url = reverse_lazy('listar-veiculos') 

class DeleteAPIVeiculos(DestroyAPIView):
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()
class FotosVeiculo(View):
    def get(self,request,arquivo):
        try:
            veiculo = Veiculo.objects.get(foto = 'veiculos/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            return FileResponse("Foto não encontrada")
        except Exception as exception:
            raise exception
        

