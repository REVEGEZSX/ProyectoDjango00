from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    resp = "<ul>"
    resp += "<li>Elemento1</li>"
    resp += "<li>Elemento2</li>"
    resp += "<li>ElementoN</li>"
    resp += "</ul>"
    return HttpResponse("<h1>"+resp+"</h1>")

def nuevoCocinero(request):
    return HttpResponse("<center><h1>ESTA ES LA PAGINA DE COCINERO</h1></center>")

def consultarPedido(request):
    return HttpResponse("<center><h1>ESTA ES LA PAGINA DE LOS PEDIDOS</h1></center>")

def platos(request):
    return HttpResponse("<center><h1>ESTA ES LA PAGINA DE LOS PLATOS</h1></center>")

def clientes(request):
    return HttpResponse("<center><h1>ESTA ES LA PAGINA DE LOS CLIENTES</h1></center>")

def consultarFacturas(request):
    return HttpResponse("<center><h1>ESTA ES LA PAGINA DE LAS FACTURAS</h1></center>")

def nuevoMesero(request):
    return HttpResponse("<center><h1>ESTA ES LA PAGINA DE LOS MESEROS</h1></center>")