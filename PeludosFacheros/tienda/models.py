from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    id              = models.AutoField(db_column='idTipo', primary_key=True) 
    nombre          = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    id              = models.AutoField(db_column='idProducto', primary_key=True) # Id unico del articulo
    nombre          = models.CharField(max_length=20) # Nombre que se muestra
    imagen          = models.CharField(max_length=500) # Imagen que se muestra
    tipo            = models.ForeignKey('TipoProducto',on_delete=models.CASCADE, db_column='idTipo') # Tipo de producto (Alimento, Ropa, Accesorios)
    precio          = models.IntegerField() # Cual es el precio actual del producto
    oferta          = models.IntegerField(blank=True, null=True) # Cuanto valia el producto ANTES DE LA OFERTA. Null si no hay ofertas
    multiples       = models.BooleanField(default=False) # Si el producto tiene varias opciones
    ofertas         = models.CharField(max_length=200, blank=True, null=True) # Las opciones del producto.

    def __str__(self):
        return str(self.nombre)+" $"+str(self.precio)