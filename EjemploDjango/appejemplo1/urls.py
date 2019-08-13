from django.contrib import admin
from django.urls import path
from appejemplo1.views import saludar,nuevoCocinero,consultarPedido,platos,consultarFacturas,nuevoMesero,clientes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', saludar),
    path('cocinero/nuevo', nuevoCocinero),
    path('pedido/', consultarPedido),
    path('platos/', platos),
    path('facturas/', consultarFacturas),
    path('meseros/', nuevoMesero),
    path('clientes/', clientes),
]