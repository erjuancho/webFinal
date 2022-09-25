from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('lacteos/', iniciolacteos, name='iniciolacteos'),
    path('galletitas/', iniciogalletitas, name='iniciogalletitas'),
    path('bebidas/', iniciobebidas, name='iniciobebidas'),
    #path('formularioProducto/', formularioProducto, name='formularioProducto'),
    path('formularioProductoApi/', formularioProductoApi, name='formularioProductoApi'),
    path('busquedaProducto/', busquedaProducto, name='busquedaProducto'),
    path('buscar/', buscar, name='buscar'),
    path('listarLacteos/', listarLacteos, name='listarLacteos'),
    path('listarGalletitas/', listarGalletitas, name='listarGalletitas'),
    path('listarBebidas/', listarBebidas, name='listarBebidas'),
    path('eliminarLacteos/<codigo>', eliminarLacteos, name='eliminarLacteos'),
    path('editarLacteos/<codigo>', editarLacteos, name='editarLacteos'),
    path('eliminarGalletitas/<codigo>', eliminarGalletitas, name='eliminarGalletitas'),
    path('eliminarBebidas/<codigo>', eliminarBebidas, name='eliminarBebidas'),
    path('login/', login_request, name='login'),

]