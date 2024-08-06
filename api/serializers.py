from rest_framework import serializers
from .models import *

# Creamos el serializer para cada modelo..


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'


class UnidadProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadProduccion
        fields = '__all__'

    def to_representation(self, instance):
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['sede'] = SedeSerializer(
                instance.sede, context=self.context).data
            return representation
        else:
            return super().to_representation(instance)


class ProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produccion
        fields = '__all__'

    def to_representation(self, instance):
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['unidadProduccion'] = UnidadProduccionSerializer(
                instance.unidadProduccion, context=self.context).data
            return representation
        else:
            return super().to_representation(instance)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'

#


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    def to_representation(self, instance):
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['unidadProduccion'] = UnidadProduccionSerializer(
                instance.unidadProduccion, context=self.context
            ).data
            representation['categoria'] = CategoriasSerializer(
                instance.categoria, context=self.context).data
            
            representation['usuario'] = UsuarioSerializer(
                instance.usuario, context=self.context).data
            return representation
        else:
            return super().to_representation(instance)


class VisitadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitado
        fields = '__all__'

    def to_representation(self, instance):
        # Verificar si 'request' está presente en el contexto
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['producto'] = ProductoSerializer(
                instance.producto, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)




class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'


    def to_representation(self, instance):
        # Verificar si 'request' está presente en el contexto
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['producto'] = ProductoSerializer(
                instance.producto, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)




class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'

    def to_representation(self, instance):
        # Verificar si 'request' está presente en el contexto
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['producto'] = ProductoSerializer(
                instance.producto, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)





class MensajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensajes
        fields = '__all__'


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = '__all__'

    def to_representation(self, instance):
        # Verificar si 'request' está presente en el contexto
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['usuario'] = UsuarioSerializer(
                instance.usuario, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)



class ImagenAnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenAnuncio
        fields = '__all__'

    def to_representation(self, instance):
        # Verificar si 'request' está presente en el contexto
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['anuncio'] = AnuncioSerializer(
                instance.anuncio, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)



class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

    def to_representation(self, instance):
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['anuncio'] = AnuncioSerializer(
                instance.anuncio, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)


class PuntoVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntoVenta
        fields = '__all__'


class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = '__all__'

    def to_representation(self, instance):
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['producto'] = ProductoSerializer(
                instance.producto, context=self.context
            ).data
            representation['puntoVenta'] = PuntoVentaSerializer(
                instance.puntoVenta, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)


class MedioPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedioPago
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

    def to_representation(self, instance):
        # Verificar si 'request' está presente en el contexto
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['usuario'] = UsuarioSerializer(
                instance.usuario, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)
        

class AuxPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxPedido
        fields = '__all__'

    def to_representation(self, instance):
        # Verificar si 'request' está presente en el contexto
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['pedido'] = PedidoSerializer(
                instance.pedido, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)
        


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

    def to_representation(self, instance):
        
        # Verificar si 'request' está presente en el contexto
        if 'request' in self.context:
            
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['medioPago'] = MedioPagoSerializer(
                instance.medioPago, context=self.context
            ).data
            representation['pedido'] = PedidoSerializer(
                instance.pedido, context=self.context).data
            
            # para terminar el bicle
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)


class DevolucionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devoluciones
        fields = '__all__'

    def to_representation(self, instance):
        # Verificar si 'request' está presente en el contexto
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['factura'] = FacturaSerializer(
                instance.factura, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'

    def to_representation(self, instance):
        # Verificar si 'request' está presente en el contexto
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['bodega'] = BodegaSerializer(
                instance.bodega, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)


class ImegenSedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenSede
        fields = '__all__'

    def to_representation(self, instance):
        # Verificar si 'request' está presente en el contexto
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['sede'] = SedeSerializer(
                instance.sede, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)


class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'

    def to_representation(self, instance):
        # Verificar si 'request' está presente en el contexto
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['anuncio'] = AnuncioSerializer(
                instance.anuncio, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)


class FotoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoUsuario
        fields = '__all__'

    def to_representation(self, instance):
        # Verificar si 'request' está presente en el contexto
        if 'request' in self.context:
            # Agregar campos adicionales para la solicitud GET
            representation = super().to_representation(instance)
            representation['usuario'] = UsuarioSerializer(
                instance.usuario, context=self.context).data
            return representation
        else:
            # En caso de que 'request' no esté en el contexto, utiliza representación predeterminada
            return super().to_representation(instance)

