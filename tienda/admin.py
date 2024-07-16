from django.contrib import admin
from .models import Producto, Usuario, Pedido, Carrito, Donacion, Tela, Ciudad, Comuna, Region

# Register your models here.
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(Carrito)
admin.site.register(Donacion)
admin.site.register(Tela)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Ciudad)