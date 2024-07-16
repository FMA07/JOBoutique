from django.db import models

# Create your models here.
class Region(models.Model):
    region          = models.CharField(max_length=30,blank=False, null=False, unique=True)
    
    def __str__(self):
        return str(self.region)
    
class Comuna(models.Model):
    comuna          = models.CharField(max_length=30,blank=False, null=False, unique=True)
    region          = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.comuna)
        
class Ciudad(models.Model):
    ciudad          = models.CharField(max_length=30,blank=False, null=False, unique=True)
    comuna          = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.ciudad)
    
class Usuario(models.Model):
    email           = models.EmailField(primary_key=True, null=False, max_length=50, unique=True)
    nombre          = models.CharField(max_length=30)
    appaterno       = models.CharField(max_length=30)
    apmaterno       = models.CharField(max_length=30)
    region          = models.ForeignKey(Region, on_delete=models.CASCADE)
    comuna          = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    ciudad          = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default='')
    direccion       = models.CharField(max_length=20)
    celular         = models.CharField(max_length=12)
    telefono_opcion = models.CharField(max_length=12, null=True, blank=True)
    contraseña     = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f'Nombre: {self.nombre} {self.appaterno} | Email: {self.email} | Comuna: {self.comuna}'

class Producto(models.Model):
    cod_producto    = models.AutoField(primary_key=True, unique=True)
    nombre          = models.CharField(max_length=50)
    precio          = models.IntegerField()
    cantidad        = models.IntegerField()
    descripcion     = models.CharField(max_length=200, null=True)
    img_producto    = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return f'Codigo producto: {self.cod_producto} | Nombre: {self.nombre} | Precio: ${self.precio} | Cantidad disponible: {self.cantidad} | Descripcion: {self.descripcion}'

class Pedido(models.Model):
    cod_pedido      = models.AutoField(primary_key=True, unique=True)
    email           = models.ForeignKey('usuario', on_delete=models.CASCADE)
    cod_tela        = models.ForeignKey('tela', to_field ='cod_tela',  on_delete=models.CASCADE)
    cod_producto    = models.ForeignKey('producto', to_field='cod_producto', on_delete=models.CASCADE)
    descripcion     = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f'Email asociado: {self.email} | Codigo_tela: {self.cod_tela} | Codigo_producto: {self.cod_producto}'
    
class Tela(models.Model):
    cod_tela        = models.CharField(max_length=5, primary_key=True, unique=True)
    img_tela        = models.ImageField(upload_to = 'telas', null = True)
    nomb_tela       = models.CharField(max_length=200, null=True)
    existencia      = models.BooleanField(default=True)
    def __str__(self):
        return f'Cod_tela: {self.cod_tela} | Nombre_tela: {self.nomb_tela} | Existencia: {self.existencia}'

class Carrito(models.Model):
    id_carrito      = models.AutoField(primary_key=True, unique=True)
    email           = models.ForeignKey('usuario', on_delete=models.CASCADE)

    def __str__(self):
        return f'Id: {self.id_carrito} | Email asociado: {self.email}'
    
class Donacion(models.Model):
    id_donacion     = models.AutoField(primary_key=True, unique=True)
    img_donacion    = models.ImageField(upload_to="donaciones", null=True)
    email           = models.ForeignKey('usuario', on_delete=models.CASCADE)

    def __str__(self):
        return f'if_donacion {self.id_donacion} | email asociado: {self.email}'