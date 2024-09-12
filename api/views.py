import json
from venv import logger
from django.http import BadHeaderError, JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
from cba.settings import EMAIL_HOST_USER
from .models import *
from .serializers import *
from django.core.mail import EmailMessage, BadHeaderError, get_connection
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page



class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'sede_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        cache.set(cache_key, response_data, timeout=60 * 15)  # Cache por 15 minutos
        return Response(response_data)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('sede_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('sede_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('sede_list')  # Limpia el caché de la lista
        return response

class UnidadProduccionViewSet(viewsets.ModelViewSet):
    queryset = UnidadProduccion.objects.all()
    serializer_class = UnidadProduccionSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'unidad_produccion_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('unidad_produccion_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('unidad_produccion_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('unidad_produccion_list')  # Limpia el caché de la lista
        return response


class ProduccionViewSet(viewsets.ModelViewSet):
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'produccion_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('produccion_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('produccion_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('produccion_list')  # Limpia el caché de la lista
        return response

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'usuario_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('usuario_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('usuario_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('usuario_list')  # Limpia el caché de la lista
        return response


class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'categoria_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('categoria_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('categoria_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('categoria_list')  # Limpia el caché de la lista
        return response


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'producto_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('producto_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('producto_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('producto_list')  # Limpia el caché de la lista
        return response


class VisitadoViewSet(viewsets.ModelViewSet):
    queryset = Visitado.objects.all()
    serializer_class = VisitadoSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'visitado_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('visitado_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('visitado_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('visitado_list')  # Limpia el caché de la lista
        return response


class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'favorito_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('favorito_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('favorito_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('favorito_list')  # Limpia el caché de la lista
        return response


class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'imagen_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('imagen_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('imagen_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('imagen_list')  # Limpia el caché de la lista
        return response


class MensajesViewSet(viewsets.ModelViewSet):
    queryset = Mensajes.objects.all()
    serializer_class = MensajesSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'mensaje_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('mensaje_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('mensaje_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('mensaje_list')  # Limpia el caché de la lista
        return response

class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'anuncio_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('anuncio_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('anuncio_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('anuncio_list')  # Limpia el caché de la lista
        return response


class ImagenAnuncioViewSet(viewsets.ModelViewSet):
    queryset = ImagenAnuncio.objects.all()
    serializer_class = ImagenAnuncioSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'img_anuncio_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('img_anuncio_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('img_anuncio_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('img_anuncio_list')  # Limpia el caché de la lista
        return response


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'comentario_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('comentario_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('comentario_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('comentario_list')  # Limpia el caché de la lista
        return response

class PuntoVentaViewSet(viewsets.ModelViewSet):
    queryset = PuntoVenta.objects.all()
    serializer_class = PuntoVentaSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'punto_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('punto_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('punto_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('punto_list')  # Limpia el caché de la lista
        return response


class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'bodega_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('bodega_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('bodega_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('bodega_list')  # Limpia el caché de la lista
        return response


class MedioPagoViewSet(viewsets.ModelViewSet):
    queryset = MedioPago.objects.all()
    serializer_class = MedioPagoSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'medio_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('medio_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('medio_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('medio_list')  # Limpia el caché de la lista
        return response


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'pedido_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('pedido_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('pedido_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('pedido_list')  # Limpia el caché de la lista
        return response

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    def list(self, request, *args, **kwargs):
        cache_key = 'factura_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('factura_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('factura_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('factura_list')  # Limpia el caché de la lista
        return response


class DevolucionesViewSet(viewsets.ModelViewSet):
    queryset = Devoluciones.objects.all()
    serializer_class = DevolucionesSerializer
    def list(self, request, *args, **kwargs):
        cache_key = 'devolucion_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('devolucion_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('devolucion_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('devolucion_list')  # Limpia el caché de la lista
        return response


class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'inventario_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('inventario_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('inventario_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('inventario_list')  # Limpia el caché de la lista
        return response

class ImagenSedeViewSet(viewsets.ModelViewSet):
    queryset = ImagenSede.objects.all()
    serializer_class = ImegenSedeSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'img_sede_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('img_sede_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('img_sede_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('img_sede_list')  # Limpia el caché de la lista
        return response


class BoletaViewSet(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer
    def list(self, request, *args, **kwargs):
        cache_key = 'boleta_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('boleta_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('boleta_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('boleta_list')  # Limpia el caché de la lista
        return response

class AuxPedidoViewSet(viewsets.ModelViewSet):
    queryset = AuxPedido.objects.all()
    serializer_class = AuxPedidoSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'aux_pedido_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('aux_pedido_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('aux_pedido_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('aux_pedido_list')  # Limpia el caché de la lista
        return response


class FotoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = FotoUsuario.objects.all()
    serializer_class = FotoUsuarioSerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'foto_usuario_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return JsonResponse(json.loads(cached_data), safe=False)
        
        response = super().list(request, *args, **kwargs)
        response_data = response.data
        
        # Serializa los datos a JSON y guarda en caché
        cache.set(cache_key, json.dumps(response_data), timeout=60 * 15)  # Cache por 15 minutos
        return JsonResponse(response_data, safe=False)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete('foto_usuario_list')  # Limpia el caché de la lista
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('foto_usuario_list')  # Limpia el caché de la lista
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('foto_usuario_list')  # Limpia el caché de la lista
        return response



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

