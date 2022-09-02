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
    producto=Bebidas(codigo=301, marca="BebidaMarca1" , sabor="Cola", precio=100)
    producto.save()
    plantilla=loader.get_template('template2.html')
    diccionario={'codigo': producto.codigo, 'marca': producto.marca, 'tipo': producto.sabor , "precio": producto.precio}
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def formularioProducto(request):

    if request.method=="POST":
        codigo=request.POST.get("codigo")
        marca=request.POST.get("marca")
        sabor=request.POST.get("sabor")
        precio=request.POST.get("precio")
        if int(str(codigo)[:1])==1:
            producto=Lacteos(codigo=codigo, marca=marca , tipo=sabor, precio=precio)
            producto.save()
            return render(request, "App1/inicio.html")
        if int(str(codigo)[:1])==2:
            producto=Galletitas(codigo=codigo, marca=marca , sabor=sabor, precio=precio)
            producto.save()
            return render(request, "App1/inicio.html")
        if int(str(codigo)[:1])==3:
            producto=Bebidas(codigo=codigo, marca=marca , sabor=sabor, precio=precio)
            producto.save()
            return render(request, "App1/inicio.html")
    return render(request, "App1/formularioProducto.html")