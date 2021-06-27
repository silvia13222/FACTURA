from django.shortcuts import render
from .models import LineaFactura, Factura
import datetime
# Create your views here.

def Listadofactura(request):
    lineafactura = LineaFactura.objects.all()

    return render(request, 'listado_factura/listado.html', {
        "lineafactura": lineafactura,
    })

def factura_funcion(request, pk):
    cliente = Factura.objects.get(id=pk)
        

    return render(request, 'listado_factura/detalle.html', {
        "cliente": cliente, 
 
    })



