
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import LineaFactura, Factura


class LineaFacturaAdmin(admin.ModelAdmin):
    search_fields = (
        'nombre_producto',
        'precio_unitario',
    )
    list_display = (
        'id',
        'nombre_producto',
        'precio_unitario',
        'unidades',
        'factura',
        
        
    )

admin.site.register(LineaFactura, LineaFacturaAdmin)


class FacturaAdmin(admin.ModelAdmin):
    search_fields = (
        'cliente_nombre',
        'fecha_emision',
        
    )
    list_display = (
        'id',
        'num',
        'cliente_nombre',
        'cliente_direccion',
        'anio',
        'fecha_emision',
    )
    list_filter = (
        'num',
       
    )

admin.site.register(Factura, FacturaAdmin)
