from django.db import models


class Sede(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, null=False, blank=False)
    ciudad = models.CharField(max_length=150, null=False, blank=False)
    departamento = models.CharField(max_length=150, null=False, blank=False)
    regional = models.CharField(max_length=150, null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    telefono1 = models.CharField(max_length=20, null=False, blank=False)
    telefono2 = models.CharField(max_length=20, null=False, blank=False)
    correo = models.CharField(max_length=100, null=False, blank=False)
    latitud = models.CharField(max_length=80, null=False, blank=False)
    longitud = models.CharField(max_length=80, null=False, blank=False)



class ImagenSede(models.Model):
    id = models.AutoField(primary_key=True)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, null=False)
    imagen = models.ImageField(upload_to='sedes-imagenes/')


class UnidadProduccion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    logo = models.ImageField(upload_to='und-prod-logos/')
    descripcion = models.TextField(null=False, blank=False)
    estado = models.BooleanField(default=True, null=False, blank=False)
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL,null=True)


class Produccion(models.Model):
    class Estado(models.TextChoices):
        CANCELADO = "CANCELADO", ("CANCELADO")
        ENVIADO = "ENVIADO", ("ENVIADO")
        PENDIENTE = "PENDIENTE", ("PENDIENTE")
        RECIBIDO = "RECIBIDO", ("RECIBIDO")
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField(null=False, blank=False)
    estado = models.CharField(max_length=20,choices=Estado.choices, default=Estado.PENDIENTE, null=False, blank=False)
    cantidad = models.IntegerField(null=False)
    fechaDespacho = models.DateTimeField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    costoProduccion = models.IntegerField(null=False, blank=False)
    fechaProduccion = models.DateField(null=False, blank=False)
    fechaVencimiento = models.DateField(null=True, blank=True)
    producto = models.IntegerField(null=False, blank=False)
    unidadProduccion = models.ForeignKey(
        UnidadProduccion, on_delete=models.SET_NULL, null=True)


class Usuario(models.Model):
    # Definición de las opciones para el campo 'tipoDocumento'
    class TipoDocumento(models.TextChoices):
        TARJETAI = "TI", ('Tarjeta de Identidad')
        CEDULA = "CC", ('Cedula de Ciudadanía')
        EXTRANGERA = "CE", ('Cedula de Extranjería')
        PASAPORTE = "PAS", ('Pasaporte')
        NIT = "NIT", ('Número de identificación tributaria')

    class Roles(models.TextChoices):
        EXTERNO = "EXTERNO", ("EXTERNO")
        APRENDIZ = "APRENDIZ", ('APRENDIZ')
        INSTRUCTOR = "INSTRUCTOR", ('INSTRUCTOR')
        FUNCIONARIO = "FUNCIONARIO", ('FUNCIONARIO')
        VENDEDOR = "VENDEDOR", ('VENDEDOR')
        TUTOR = "TUTOR", ('TUTOR')
        LIDER = "LIDER", ('LIDER')
        PUNTO = "PUNTO", ('PUNTO')

    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=150, blank=False, null=False)
    apellidos = models.CharField(max_length=150, blank=False, null=False)
    tipoDocumento = models.CharField(
        max_length=3,
        choices=TipoDocumento.choices, default=TipoDocumento.CEDULA)
    numeroDocumento = models.CharField(max_length=20, blank=False, null=False)
    correoElectronico = models.CharField(
        max_length=100, blank=False, null=False)
    ciudad = models.CharField(max_length=150, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    telefonoCelular = models.CharField(max_length=12, blank=True, null=True)
    rol1 = models.CharField(
        max_length=15, choices=Roles.choices, default=Roles.APRENDIZ, blank=True, null=True)
    rol2 = models.CharField(
        max_length=15, choices=Roles.choices, default=Roles.APRENDIZ, blank=True, null=True)
    rol3 = models.CharField(
        max_length=15, choices=Roles.choices, default=Roles.APRENDIZ, blank=True, null=True)
    estado = models.BooleanField(default=True, blank=False, null=False)
    cargo = models.CharField(max_length=150, blank=True, null=True)
    ficha = models.CharField(max_length=7, null=True, blank=True)
    vocero = models.BooleanField(default=False, blank=True, null=True)
    fechaRegistro = models.DateField(blank=False, null=False, auto_now_add=True)
    sede = models.IntegerField(null=True, blank=True)
    puntoVenta = models.IntegerField(null=True, blank=True)
    unidadProduccion = models.IntegerField(null=True, blank=True)

class FotoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE )
    foto = models.ImageField(upload_to='usuarios-fotos/')


class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    imagen = models.ImageField(upload_to='categorias-imagenes/')
    icono = models.FileField(upload_to='categorias-iconos/')


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    estado = models.BooleanField(default=False, blank=False)
    maxReserva = models.IntegerField(null=True, blank=True)
    unidadMedida = models.CharField(max_length=50, null=False, blank=False)
    destacado = models.BooleanField(default=False, null=True, blank=True)
    precio = models.IntegerField(null=False, blank=False)
    precioAprendiz = models.IntegerField(null=True, blank=True)
    precioInstructor = models.IntegerField(null=True, blank=True)
    precioFuncionario = models.IntegerField(null=True, blank=True)
    precioOferta = models.IntegerField(null=False, blank=False)
    exclusivo = models.BooleanField(default=False)
    categoria = models.ForeignKey(
        Categorias, on_delete=models.SET_NULL, null=True)
    unidadProduccion = models.ForeignKey(
        UnidadProduccion,  on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, null=False)
    


class Visitado(models.Model):
    id = models.AutoField(primary_key=True)
    fechaVista = models.DateField(null=False, blank=False, auto_now_add=True)
    usuario = models.IntegerField(null=False, blank=False)
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, null=False)


class Favorito(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.IntegerField(null=False, blank=False)
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, null=False)


class Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='productos-imagenes/')
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, null=False)


class Mensajes(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(null=False, blank=False)
    contenido = models.TextField(null=False, blank=False)
    usuarioEmisor = models.IntegerField(null=False, blank=False)
    usuarioReceptor = models.IntegerField(null=False, blank=False)


class Anuncio(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    fecha = models.DateTimeField(null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    fechaEvento = models.DateTimeField(null=False)
    evento = models.BooleanField(default=False)
    eventoIncripcionInicio = models.DateTimeField(null=True)
    eventoIncripcionFin = models.DateTimeField(null=True)
    maxcupos = models.IntegerField(null=True)
    anexo = models.FileField(upload_to='anuncios-anexo/' ,null=True)


class ImagenAnuncio(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='anuncios-imagenes/')
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, null=False)


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(null=False, blank=False)
    fecha = models.DateTimeField(null=False, blank=False)
    usuario = models.IntegerField(null=False, blank=False)
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, null=False)


class PuntoVenta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    ubicacion = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(default=True, null=False, blank=False)
    sede = models.IntegerField(null=False, blank=False)


class Bodega(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(null=False, blank=False)
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, null=False)
    puntoVenta = models.ForeignKey(
        PuntoVenta, on_delete=models.CASCADE, null=False)


class MedioPago(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    detalle = models.TextField(null=False, blank=False)



class Pedido(models.Model):
    class Estado(models.TextChoices):
        CANCELADO = "CANCELADO", ("CANCELADO")
        PENDIENTE = "PENDIENTE", ("PENDIENTE")
        COMPLETADO = "COMPLETADO", ("COMPLETADO")

    id = models.AutoField(primary_key=True)
    numeroPedido = models.IntegerField(null=False, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    fechaEncargo = models.DateTimeField(null=True, blank=True)
    fechaEntrega = models.DateTimeField(null=True, blank=True)
    grupal = models.BooleanField(default=False, null=True, blank=True)
    estado = models.CharField(
        max_length=50, choices=Estado.choices
    )
    entregado = models.BooleanField(default=False, null=True, blank=True)
    puntoVenta = models.IntegerField(null=True, blank=True)
    pedidoConfirmado = models.BooleanField(default=False, null=False)

class AuxPedido(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    producto = models.IntegerField(null=False, blank=False)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=False)

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField(null=False, blank=False)
    fecha = models.DateTimeField(null=False, blank=False)
    usuarioVendedor= models.CharField(null=False, blank=False, default=0)
    medioPago = models.ForeignKey(
        MedioPago, on_delete=models.CASCADE, null=False)
    pedido = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, null=False)


class Devoluciones(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(null=False, blank=False)
    estado = models.BooleanField(default=False, null=True, blank=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, null=False)


class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    stock = models.IntegerField(null=False, blank=False)
    fecha = models.DateTimeField(null=False, blank=False)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=False)
    produccion = models.IntegerField(null=False, blank=False, default=0)


class Boleta(models.Model):
    id = models.AutoField(primary_key=True)
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, null=False)
    usuario = models.IntegerField(null=False, blank=False)
    
