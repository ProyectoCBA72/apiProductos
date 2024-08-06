from django.urls import path, include
from rest_framework import routers
from .views import *

# Definimos un enrutador
router = routers.DefaultRouter()

# Registrando las URL para cada ViewSet con el basename correspondiente
router.register(r'sedes', SedeViewSet, basename='sede')
router.register(r'imagenes-sede',  ImagenSedeViewSet, basename='imagen-sede')
router.register(r'unidades-produccion', UnidadProduccionViewSet,
                basename='unidad-produccion')
router.register(r'producciones', ProduccionViewSet, basename='produccion')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'categorias', CategoriasViewSet, basename='categoria')
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'visitados', VisitadoViewSet, basename='visitado')
router.register(r'favoritos', FavoritoViewSet, basename='favorito')
router.register(r'imagenes', ImagenViewSet, basename='imagen')
router.register(r'mensajes', MensajesViewSet, basename='mensaje')
router.register(r'anuncios', AnuncioViewSet, basename='anuncio')
router.register(r'imagenes-anuncio', ImagenAnuncioViewSet,
                basename='imagen-anuncio')
router.register(r'comentarios', ComentarioViewSet, basename='comentario')
router.register(r'puntos-venta', PuntoVentaViewSet, basename='punto-venta')
router.register(r'bodegas', BodegaViewSet, basename='bodega')
router.register(r'medios-pago', MedioPagoViewSet, basename='medio-pago')
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'facturas', FacturaViewSet, basename='factura')
router.register(r'devoluciones', DevolucionesViewSet, basename='devolucion')
router.register(r'inventarios', InventarioViewSet, basename='inventario')
router.register(r'boletas', BoletaViewSet, basename='boleta')
router.register(r'foto-usuarios', FotoUsuarioViewSet, basename='foto-usuario')
router.register(r'aux-pedidos', AuxPedidoViewSet, basename='aux-pedido')


urlpatterns = [
    path('', include(router.urls)),
    path('send-email/', send_email, name='send-email'),
]


urlpatterns += router.urls
