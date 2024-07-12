from django.shortcuts import render, get_object_or_404
from .models import TipoProducto, Producto

# Create your views here.
def index(request):
    context={"mensaje": "Texto de relleno blablabla"}
    return render(request, 'tienda/index.html', context)

def contacto(request):
    context={"mensaje": "Texto de relleno blablabla"}
    return render(request, 'tienda/contacto.html', context)

def nosotros(request):
    context={"mensaje": "Texto de relleno blablabla"}
    return render(request, 'tienda/nosotros.html', context)

def donaciones(request):
    context={"mensaje": "Texto de relleno blablabla"}
    return render(request, 'tienda/donaciones.html', context)

def tiendaaccesorios(request):
    # TODO: Hacer lo mismo que con alimentos
    context={"mensaje": "Texto de relleno blablabla"}
    return render(request, 'tienda/tiendaaccesorios.html', context)

def tiendaalimentos(request):
    product_type = get_object_or_404(TipoProducto, nombre='Alimento')
    productos = Producto.objects.filter(tipo = product_type)
    context={'productos' : productos}
    return render(request, 'tienda/tiendaalimentos.html', context)
    #return render(request, 'tienda/tiendaalimentos.html', {})

def tiendaropas(request):
    # TODO: Hacer lo mismo que con alimentos.
    context={"mensaje": "Texto de relleno blablabla"}
    return render(request, 'tienda/tiendaropas.html', context)