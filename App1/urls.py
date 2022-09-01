from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('lacteos/', iniciolacteos),
    path('galletitas/', iniciogalletitas),
    path('bebidas/', iniciobebidas),
]