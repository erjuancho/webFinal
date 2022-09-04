from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from .models import Bebidas, Galletitas, Lacteos
from django.template import Context, Template, loader
from App1.forms import FormularioProductoApi



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
    diccionario={'codigo': producto.codigo, 'marca': producto.marca, 'tipo': producto.tipo , "precio": producto.precio}
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def bebidas(request):
    producto=Bebidas(codigo=301, marca="BebidaMarca1" , sabor="Cola", precio=100)
    producto.save()
    plantilla=loader.get_template('template2.html')
    diccionario={'codigo': producto.codigo, 'marca': producto.marca, 'tipo': producto.tipo , "precio": producto.precio}
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def formularioProducto(request):

    if request.method=="POST":
        codigo=request.POST.get("codigo")
        marca=request.POST.get("marca")
        tipo=request.POST.get("tipo")
        precio=request.POST.get("precio")
        if int(str(codigo)[:1])==1:
            producto=Lacteos(codigo=codigo, marca=marca , tipo=tipo, precio=precio)
            producto.save()
            return render(request, "App1/inicio.html")
        if int(str(codigo)[:1])==2:
            producto=Galletitas(codigo=codigo, marca=marca , tipo=tipo, precio=precio)
            producto.save()
            return render(request, "App1/inicio.html")
        if int(str(codigo)[:1])==3:
            producto=Bebidas(codigo=codigo, marca=marca , tipo=tipo, precio=precio)
            producto.save()
            return render(request, "App1/inicio.html")
        return render(request, "App1/formularioError.html")
    return render(request, "App1/formularioProducto.html")


def formularioProductoApi(request):

    if request.method=="POST":
        formulario=FormularioProductoApi(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            codigo=data.get("codigo")
            marca=data.get("marca")
            tipo=data.get("tipo")
            precio=data.get("precio")
            if int(str(codigo)[:1])==1:
                producto=Lacteos(codigo=codigo, marca=marca , tipo=tipo, precio=precio)
                producto.save()
                return render(request, "App1/inicio.html", {"mensaje": "Producto creado con exito"})
            if int(str(codigo)[:1])==2:
                producto=Galletitas(codigo=codigo, marca=marca , tipo=tipo, precio=precio)
                producto.save()
                return render(request, "App1/inicio.html", {"mensaje": "Producto creado con exito"})
            if int(str(codigo)[:1])==3:
                producto=Bebidas(codigo=codigo, marca=marca , tipo=tipo, precio=precio)
                producto.save()
                return render(request, "App1/inicio.html", {"mensaje": "Producto creado con exito"})
            return render(request, "App1/formularioError.html")
        else:
            return render(request, "App1/formularioError.html")
    else:
         formulario=FormularioProductoApi()
         return render(request, "App1/formularioProductoApi.html", {"formulario": formulario})


def busquedaProducto(request):
    return render(request, "App1/busquedaProducto.html")

def buscar(request):
    producto=request.GET.get("codigo")
    if int(str(producto)[:1])==1:
        lacteos=Lacteos.objects.filter(codigo=producto)
        return render(request, "App1/resultadoBusqueda.html", {"productos":lacteos})
    if int(str(producto)[:1])==2:
        galletitas=Galletitas.objects.filter(codigo=producto)
        return render(request, "App1/resultadoBusqueda.html", {"productos":galletitas})
    if int(str(producto)[:1])==3:
        bebidas=Bebidas.objects.filter(codigo=producto)
        return render(request, "App1/resultadoBusqueda.html", {"productos":bebidas})
    return render(request, "App1/formularioError.html")
