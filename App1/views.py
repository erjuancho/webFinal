from django.shortcuts import render
from django.http import HttpResponse
from .models import Bebidas, Galletitas, Lacteos
from django.template import Context, Template, loader



# Create your views here.

def inicio(request):
    return render(request,"App1/inicio.html")

def iniciolacteos(request):
    return render(request,"App1/lacteos.html")

def iniciogalletitas(request):
    return render(request,"App1/galletitas.html")

def iniciobebidas(request):
    return render(request,"App1/bebidas.html")


def lacteos(request):
    producto=Lacteos(codigo=101, marca="LechaMarca1" , tipo="Descremada", precio=100)
    producto.save()
    plantilla=loader.get_template('template1.html')
    diccionario={'codigo': producto.codigo, 'marca': producto.marca, 'tipo': producto.tipo , "precio": producto.precio}
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def galletitas(request):
    producto=Galletitas(codigo=201, marca="GalletitaMarca1" , sabor="Chocolate", precio=100)
    producto.save()
    plantilla=loader.get_template('template2.html')
    diccionario={'codigo': producto.codigo, 'marca': producto.marca, 'tipo': producto.sabor , "precio": producto.precio}
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def bebidas(request):
    producto=Bebidas(codigo=201, marca="BebidaMarca1" , sabor="Cola", precio=100)
    producto.save()
    plantilla=loader.get_template('template2.html')
    diccionario={'codigo': producto.codigo, 'marca': producto.marca, 'tipo': producto.sabor , "precio": producto.precio}
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
