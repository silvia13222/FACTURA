from django.db import models
import datetime

import math
# Create your models here.


# Create your models here.
class Factura(models.Model):

    num = models.CharField(max_length=100, unique=True)
    cliente_nombre = models.CharField(max_length=100, unique=True)
    cliente_direccion = models.CharField(max_length=100,  blank=True) 
    anio = models.IntegerField(default=datetime.datetime.now().year)
    fecha_emision = models.DateField(max_length=100)
    

    
    def __str__(self):
        return f'{self.cliente_nombre}, {self.num}'

class LineaFactura(models.Model): #N:1

    nombre_producto = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_length=100, max_digits=5, decimal_places=2)
    unidades = models.PositiveIntegerField(default=1)
    precio_compra = models.DecimalField(max_length=100, max_digits=5, decimal_places=2)
    factura = models.ForeignKey(
        Factura,
        null=True,  #te permite que no tenga
        blank=True, #te permite que esté en blanco
        on_delete=models.PROTECT,  #siborro el equipo que pasa? proteger
    
    )
    def precio_compra(self):
        compra = (self.precio_unitario*self.unidades) 
        return compra


    def __str__(self):
        
        return f"{self.nombre_producto}, {self.unidades}, [{self.factura}]"


