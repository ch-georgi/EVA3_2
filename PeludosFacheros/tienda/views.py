from django.shortcuts import render, get_object_or_404
from .models import TipoProducto, Producto, VariacionProducto
from .forms import TipoProductoForm, ProductoForm, VariacionProductoForm

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
    product_type = get_object_or_404(TipoProducto, id=3)
    productos = Producto.objects.filter(tipo = product_type)
    context={'productos' : productos, 'categoria' : 'Alimentos'}
    return render(request, 'tienda/tienda.html', context)

def tiendaalimentos(request):
    product_type = get_object_or_404(TipoProducto, id=1)
    productos = Producto.objects.filter(tipo = product_type)
    context={'productos' : productos, 'categoria' : 'Alimentos'}
    return render(request, 'tienda/tienda.html', context)

def tiendaropas(request):
    product_type = get_object_or_404(TipoProducto, id=2)
    productos = Producto.objects.filter(tipo = product_type)
    context={'productos' : productos, 'categoria' : 'Ropa'}
    return render(request, 'tienda/tienda.html', context)

def mantenedorproductos(request):
    productos = Producto.objects.all()
    context = {"productos" : productos}
    return render(request,'tienda/productosall.html', context)

def agregarproductos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            productos = Producto.objects.all()
            context = {"productos" : productos}
            return render(request,'tienda/productosall.html', context)
    else:
        form = ProductoForm()
    return render(request, 'tienda/productosForm.html', {'form': form})