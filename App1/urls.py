from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('lacteos/', iniciolacteos, name='iniciolacteos'),
    path('galletitas/', iniciogalletitas, name='iniciogalletitas'),
    path('bebidas/', iniciobebidas, name='iniciobebidas'),
]