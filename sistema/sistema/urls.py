from django.contrib import admin
from django.urls import path, include
from sistema.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('veiculos/', include('veiculos.urls'), name='veiculos')
]