from django.contrib import admin
from django.urls import path, include
from sistema.views import Login, Logout, LoginAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('veiculos/', include('veiculos.urls'), name='veiculos'),
    path('anuncios/',include('anuncios.urls')),
    path('autenticacao-api/',LoginAPI.as_view()),
]