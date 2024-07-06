from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('tiendaaccesorios', views.tiendaaccesorios, name='tiendaaccesorios'),
    path('tiendaalimentos', views.tiendaalimentos, name='tiendaalimentos'),
    path('tiendaropas', views.tiendaropas, name='tiendaropas'),
]