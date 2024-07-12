from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    id              = models.AutoField(db_column='idTipo', primary_key=True) 
    nombre          = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nombre)
    
class VariacionProducto(models.Model):
    id              = models.AutoField(db_column='idVariacion', primary_key=True) 
    nombreVariacion          = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nombreVariacion)

class Producto(models.Model):
    id              = models.AutoField(db_column='idProducto', primary_key=True) # Id unico del articulo
    nombre          = models.CharField(max_length=200) # Nombre que se muestra
    imagen          = models.ImageField(upload_to='imagenes/')
    tipo            = models.ForeignKey('TipoProducto',on_delete=models.CASCADE, db_column='idTipo') # Tipo de producto (Alimento, Ropa, Accesorios)
    precio          = models.IntegerField() # Cual es el precio actual del producto
    oferta          = models.IntegerField(blank=True, null=True) # Cuanto valia el producto ANTES DE LA OFERTA. Null si no hay ofertas
    idVariacion     = models.ForeignKey('VariacionProducto',on_delete=models.SET_NULL , db_column='idVariacion',blank=True, null=True) # Si el producto tiene varias opciones
    stock           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" $"+str(self.precio)
    