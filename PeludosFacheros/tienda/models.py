from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    id              = models.AutoField(db_column='idTipo', primary_key=True) 
    nombre          = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    id              = models.AutoField(db_column='idProducto', primary_key=True) 
    nombre          = models.CharField(max_length=20)
    imagen          = models.CharField(max_length=500)
    tipo            = models.ForeignKey('Tipo',on_delete=models.CASCADE, db_column='idTipo')
    precio          = models.IntegerField()
    oferta          = models.IntegerField()
    precio_anterior = models.IntegerField( blank=True, null=True)
    multiple        = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" $"+str(self.precio)