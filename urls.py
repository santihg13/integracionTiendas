"""
URL configuration for integracionTiendas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, register_converter
from . import views
from soapbox import soap_dispatch


class FloatConverter:
    regex = '[0-9]+(\.[0-9]+)?'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)

register_converter(FloatConverter, 'float')

class RegistroVentaService:
    @soap_dispatch.bind('RegistrarVenta')
    def registrar_venta(self, nombre_aplicacion, id_tienda, monto_venta, nombre_vista):
        # Lógica para registrar la venta
        return "Venta registrada correctamente"

urlpatterns = [
    path('ventas/<str:nombre_aplicacion>/<int:id_tienda>/<float:monto_venta>/<str:nombre_vista>/', views.registrar_venta),
    path('ventas/soap/', RegistroVentaService.registrar_venta, name='registrar_venta_soap'),
    path('my-view/', views.my_view, name='my-view'),
    path('', views.index, name='index'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]