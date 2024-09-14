import json
from django.http import BadHeaderError, JsonResponse
from rest_framework import viewsets
from cba.settings import EMAIL_HOST_USER
from .models import *
from .serializers import *
from django.core.mail import EmailMessage, BadHeaderError, get_connection
from django.views.decorators.csrf import csrf_exempt

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer


class UnidadProduccionViewSet(viewsets.ModelViewSet):
    queryset = UnidadProduccion.objects.all()
    serializer_class = UnidadProduccionSerializer


class ProduccionViewSet(viewsets.ModelViewSet):
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class VisitadoViewSet(viewsets.ModelViewSet):
    queryset = Visitado.objects.all()
    serializer_class = VisitadoSerializer


class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer


class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer


class MensajesViewSet(viewsets.ModelViewSet):
    queryset = Mensajes.objects.all()
    serializer_class = MensajesSerializer


class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer


class ImagenAnuncioViewSet(viewsets.ModelViewSet):
    queryset = ImagenAnuncio.objects.all()
    serializer_class = ImagenAnuncioSerializer



class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class PuntoVentaViewSet(viewsets.ModelViewSet):
    queryset = PuntoVenta.objects.all()
    serializer_class = PuntoVentaSerializer


class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer


class MedioPagoViewSet(viewsets.ModelViewSet):
    queryset = MedioPago.objects.all()
    serializer_class = MedioPagoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer


class DevolucionesViewSet(viewsets.ModelViewSet):
    queryset = Devoluciones.objects.all()
    serializer_class = DevolucionesSerializer


class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer



class ImagenSedeViewSet(viewsets.ModelViewSet):
    queryset = ImagenSede.objects.all()
    serializer_class = ImegenSedeSerializer



class BoletaViewSet(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class AuxPedidoViewSet(viewsets.ModelViewSet):
    queryset = AuxPedido.objects.all()
    serializer_class = AuxPedidoSerializer


class FotoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = FotoUsuario.objects.all()
    serializer_class = FotoUsuarioSerializer


@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            subject = data.get("subject", "")
            message = data.get("message", "")
            from_email = EMAIL_HOST_USER
            recipient_list = data.get("recipient_list", "")

            if subject and message and from_email and recipient_list:
                try:
                    email = EmailMessage(
                        subject,
                        message,
                        from_email,
                        recipient_list.split(),  # Convertir la lista de destinatarios a una lista de Python
                        connection=get_connection()
                    )
                    email.send()
                    return JsonResponse({"message": "Correo electrónico enviado exitosamente"}, status=200)
                except BadHeaderError:
                    return JsonResponse({"error": "Error al enviar correo electrónico"}, status=400)
            else:
                return JsonResponse({"error": "Por favor, complete todos los campos"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Error al procesar la solicitud JSON"}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)

