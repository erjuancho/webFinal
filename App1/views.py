from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from .models import Bebidas, Galletitas, Lacteos
from django.template import Context, Template, loader
from App1.forms import FormularioProductoApi
from django.views.generic import ListView



# Create your views here.

def inicio(request):
    return render(request,"App1/inicio.html")

def iniciolacteos(request):
    return render(request,"App1/lacteos.html")

def iniciogalletitas(request):
    return render(request,"App1/galletitas.html")

def iniciobebidas(request):
    return render(request,"App1/bebidas.html")

'''
def formularioProducto(request):

    if request.method=="POST":
        codigo=request.POST.get("codigo")
        marca=request.POST.get("marca")
        tipo=request.POST.get("tipo")
        precio=request.POST.get("precio")
        cantidad=request.POST.get("cantidad")
        if int(str(codigo)[:1])==1:
            producto=Lacteos(codigo=codigo, marca=marca , tipo=tipo, precio=precio, cantidad=cantidad)
            producto.save()
            return render(request, "App1/formularioExito.html")
        if int(str(codigo)[:1])==2:
            producto=Galletitas(codigo=codigo, marca=marca , tipo=tipo, precio=precio, cantidad=cantidad)
            producto.save()
            return render(request, "App1/formularioExito.html")
        if int(str(codigo)[:1])==3:
            producto=Bebidas(codigo=codigo, marca=marca , tipo=tipo, precio=precio, cantidad=cantidad)
            producto.save()
            return render(request, "App1/formularioExito.html")
        return render(request, "App1/formularioError.html")
    return render(request, "App1/formularioProducto.html")
'''


def formularioProductoApi(request):

    if request.method=="POST":
        formulario=FormularioProductoApi(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            codigo=data.get("codigo")
            marca=data.get("marca")
            tipo=data.get("tipo")
            precio=data.get("precio")
            cantidad=data.get("cantidad")
            if int(str(codigo)[:1])==1:
                lista=Lacteos.objects.filter(codigo=codigo)
                if len(lista) != 0:
                    return render(request, "App1/formularioErrorExiste.html")
                else:
                    producto=Lacteos(codigo=codigo, marca=marca , tipo=tipo, precio=precio, cantidad=cantidad)
                    producto.save()
                    return render(request, "App1/formularioExito.html")
            if int(str(codigo)[:1])==2:
                lista=Galletitas.objects.filter(codigo=codigo)
                if len(lista) != 0:
                    return render(request, "App1/formularioErrorExiste.html")
                else:
                    producto=Galletitas(codigo=codigo, marca=marca , tipo=tipo, precio=precio, cantidad=cantidad)
                    producto.save()
                    return render(request, "App1/formularioExito.html")
            if int(str(codigo)[:1])==3:
                lista=Lacteos.objects.filter(codigo=codigo)
                if len(lista) != 0:
                    return render(request, "App1/formularioErrorExiste.html")
                else:
                    producto=Bebidas(codigo=codigo, marca=marca , tipo=tipo, precio=precio, cantidad=cantidad)
                    producto.save()
                    return render(request, "App1/formularioExito.html")
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

def listarLacteos(request):
    lacteos=Lacteos.objects.all()
    return render(request, "App1/listarLacteos.html", {"lacteos":lacteos})

def listarGalletitas(request):
    galletitas=Galletitas.objects.all()
    return render(request, "App1/listarGalletitas.html", {"galletitas":galletitas})

def listarBebidas(request):
    bebidas=Bebidas.objects.all()
    return render(request, "App1/listarBebidas.html", {"bebidas":bebidas})

def eliminarLacteos(request, codigo):
    producto=Lacteos.objects.get(codigo=codigo)
    producto.delete()
    lacteos=Lacteos.objects.all()
    return render(request, "App1/listarLacteos.html", {"lacteos":lacteos})

def eliminarGalletitas(request, codigo):
    producto=Galletitas.objects.get(codigo=codigo)
    producto.delete()
    galletitas=Galletitas.objects.all()
    return render(request, "App1/listarGalletitas.html", {"galletitas":galletitas})

def eliminarBebidas(request, codigo):
    producto=Bebidas.objects.get(codigo=codigo)
    producto.delete()
    bebidas=Bebidas.objects.all()
    return render(request, "App1/listarBebidas.html", {"bebidas":bebidas})

def editarLacteos(request, codigo):
    producto=Lacteos.objects.get(codigo=codigo)
    if request.method=="POST":
        form=FormularioProductoApi(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            producto.codigo=info["codigo"]
            producto.marca=info["marca"]
            producto.tipo=info["tipo"]
            producto.precio=info["precio"]
            producto.cantidad=info["cantidad"]
            producto.save()
            lacteos=Lacteos.objects.all()
            return render(request, "App1/listarLacteos.html", {"lacteos":lacteos})
    else:
        form=FormularioProductoApi(initial={"codigo":producto.codigo, "marca":producto.marca, "tipo":producto.tipo, "precio":producto.precio , "cantidad":producto.cantidad})
        return render(request, "App1/editarLacteos.html", {"formulario":form, "codigo_producto":producto.codigo })



    



    


