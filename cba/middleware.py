from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
import json

class CustomCacheMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Solo manejar GET para caché
        if request.method == 'GET':
            cache_key = self.get_cache_key(request)
            cached_response = cache.get(cache_key)
            if cached_response:
                # Devuelve una respuesta simulada a partir del contenido en caché
                return HttpResponse(cached_response, content_type='application/json')

    def process_response(self, request, response):
        if request.method == 'GET' and response.status_code == 200:
            cache_key = self.get_cache_key(request)
            cache.set(cache_key, response.content, timeout=60 * 15)  # Cache por 15 minutos
        elif request.method in ['POST', 'PUT', 'DELETE']:
            # Elimina el caché asociado a la URL base
            cache_key = self.get_cache_key(request, clear=True)
            cache.delete(cache_key)
        return response

    def get_cache_key(self, request, clear=False):
        # Construye una clave de caché basada en la URL y el método HTTP
        if clear:
            # Si estamos limpiando caché, eliminamos el parámetro de ID de la URL
            return request.path
        return request.get_full_path()

    def clear_related_cache(self, request):
        # Limpia el caché para todas las URLs relacionadas si es necesario
        base_url = request.path.split('/')[1]  # Obtiene la URL base para el caché
        cache_keys = [base_url]
        for key in cache_keys:
            cache.delete(key)
