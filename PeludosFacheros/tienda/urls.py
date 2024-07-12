from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('donaciones', views.donaciones, name='donaciones'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('tiendaalimentos', views.tiendaalimentos, name='tiendaalimentos'),
    path('tiendaropas', views.tiendaropas, name='tiendaropas'),
    path('tiendaaccesorios', views.tiendaaccesorios, name='tiendaaccesorios'),
    path('productos', views.mantenedorproductos, name='mantenedorproductos'),
]