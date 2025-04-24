from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

class Login(View):

    def get(self,request):
        contexto ={'mensagem': ''}
        if request.user.is_authenticated:
            return redirect("listar-veiculos")
        else:
            return render(request, 'autenticacao.html', contexto)

    def post(self, request):
        usuario = request.POST.get('email', None)
        senha = request.POST.get('password', None)

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("listar-veiculos")
        
            return render(request, 'autenticacao.html', {'mensagem':'Usuário inativo!'})
        return render(request, 'autenticacao.html', {'mensagem':'Usuário e senha inválidos!'})
    
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("login")