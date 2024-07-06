from django.shortcuts import render
from .models import TipoProducto, Producto

# Create your views here.
def index(request):
    context={"mensaje": "Texto de relleno blablabla"}
    return render(request, 'tienda/index.html', context)

def tiendaaccesorios(request):
    context={"mensaje": "Texto de relleno blablabla"}
    return render(request, 'tienda/tiendaaccesorios.html', context)

def tiendaalimentos(request):
    context={"mensaje": "Texto de relleno blablabla"}
    return render(request, 'tienda/tiendaalimentos.html', context)

def tiendaropas(request):
    context={"mensaje": "Texto de relleno blablabla"}
    return render(request, 'tienda/tiendaropas.html', context)