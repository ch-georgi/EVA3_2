from django import forms
from django.utils import timezone
from django.forms import ModelForm
from .models import TipoProducto,VariacionProducto,Producto

class TipoProductoForm(ModelForm):
    class Meta:
        model = TipoProducto
        fields = [
            "id",
            "nombre"
        ]
        labels = {
            "nombre" : "Tipo de producto"
        }
        exclude = ["id"]

class VariacionProductoForm(ModelForm):
    class Meta:
        model = VariacionProducto
        fields = [
            "id",
            "nombreVariacion"
        ]
        labels = {
            "nombreVariacion" : "Familia de producto"
        }
        exclude = ["id"]

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = [
            "id",
            "nombre",
            "imagen",
            "tipo",
            "precio",
            "oferta",
            "idVariacion",
            "stock"
        ]
        labels = {
            "nombre" : "Nombre de producto",
            "tipo" : "Tipo de producto",
            "idVariacion" : "Familia de producto"
        }
        exclude = ["id"]