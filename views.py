from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import zeep

@csrf_exempt
def registrar_venta(request, nombre_aplicacion, id_tienda, monto_venta, nombre_vista):
    if id_tienda == 1:
        # SOAP
        wsdl_url = 'http://ejemplo.com/soap/service?wsdl'
        client = zeep.Client(wsdl=wsdl_url)

        try:
            response = client.service.RegistrarVenta(nombre_aplicacion, id_tienda, monto_venta, nombre_vista)
            return HttpResponse("Venta registrada correctamente")
        except Exception as e:
            return HttpResponse("Error al registrar la venta: " + str(e))

    else:
        # RESTful
        api_url = 'http://ejemplo.com/api/v1/ventas'

        try:
            response = requests.post(api_url, json={'nombre_aplicacion': nombre_aplicacion,
                                                    'id_tienda': id_tienda,
                                                    'monto_venta': monto_venta,
                                                    'nombre_vista': nombre_vista})

            if response.status_code == 201:
                return HttpResponse("Venta registrada correctamente")
            else:
                return HttpResponse("Error al registrar la venta")
        except requests.exceptions.RequestException as e:
            return HttpResponse("Error al comunicarse con la API: " + str(e))

from django.http import JsonResponse

def my_view(request):
    # Realiza la conexión al servicio RESTful
    response = requests.get('http://ejemplo.com/api/endpoint')

    if response.status_code == 200:
        # La solicitud fue exitosa
        data = response.json()
        # Procesa los datos recibidos
        return JsonResponse(data)  # Devuelve los datos como una respuesta JSON
    else:
        # Ocurrió un error en la solicitud
        error_message = response.text
        # Maneja el error según tus necesidades
        return JsonResponse({'error': error_message}, status=response.status_code)  # Devuelve un mensaje de error en JSON

def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})