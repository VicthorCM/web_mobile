from django.test import TestCase
from django.contrib.auth.models import User
from .models import Veiculo
from .forms import VeiculoForm
from datetime import datetime
from django.urls import reverse_lazy,reverse

class TestesModelVeiculo(TestCase):
    
    def setUp(self):
        self.instancia = Veiculo(
            marca=1,
            modelo = "ABCD",
            ano = datetime.now().year,
            cor = 2,
            combustivel =3
        )

    def test_is_now(self):
        self.assertTrue(self.instancia.veiculo_novo)
        self.instancia.ano = datetime.now().year - 5
        self.assertFalse(self.instancia.veiculo_novo)
    
    def test_years_use(self):
        self.instancia.ano= datetime.now().year - 10
        self.assertEqual(self.instancia.anos_de_uso(),10)

class TestesViewsListarVeiculos(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username = "teste", password="12345678")
        self.client.force_login(self.user)
        self.url = reverse_lazy('listar-veiculos')
        Veiculo(marca=1,modelo = "ABCD", ano = 2, cor = 3, combustivel = 1, foto='foto.jpeg').save()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.context.get('veiculos')),1)

class TestesViewsCriarVeiculos(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username = "teste", password="12345678")
        self.client.force_login(self.user)
        self.url = reverse_lazy('cadastrar-veiculos')
        

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(response.context.get('form'),VeiculoForm)

    def test_post(self):
        data ={ 'marca':1, 'modelo': 'ABCD', 'ano':2,'cor':2, 'combustivel':3}
        response = self.client.post(self.url,data)

        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('listar-veiculos'))

        self.assertEqual(Veiculo.objects.count(),1)
        self.assertEqual(Veiculo.objects.first().modelo,"ABCD")

class TestesViewEditarVeiculos(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username = "teste", password="12345678")
        self.client.force_login(self.user)
        self.instacia= Veiculo.objects.create(marca=1,modelo = "ABCD", ano = 2, cor = 3, combustivel = 1, foto='foto.jpeg')
        self.url = reverse('editar-veiculos',kwargs={'pk':self.instacia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(response.context.get('object'),Veiculo)
        self.assertIsInstance(response.context.get('form'),VeiculoForm)
        self.assertEqual(response.context.get('object').pk,self.instacia.pk)
        self.assertEqual(response.context.get('object').marca,self.instacia.marca)
    
    # def test_post(self):


class TestesViewsDeletarVeiculos(TestCase):

    def setUp(self):
        self.user = User.objects.create(username = "teste", password="12345678")
        self.client.force_login(self.user)
        self.instacia= Veiculo.objects.create(marca=1,modelo = "ABCD", ano = 2, cor = 3, combustivel = 1, foto='foto.jpeg')
        self.url = reverse('excluir-veiculos',kwargs={'pk':self.instacia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(response.context.get('object'),Veiculo)
        self.assertEqual(response.context.get('object').pk,self.instacia.pk)
    
    def test_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(),0)
        


        