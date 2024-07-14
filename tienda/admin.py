from django.contrib import admin
from .models import Producto, Usuario, Pedido, Carrito, Donacion, Tela

# Register your models here.
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(Carrito)
admin.site.register(Donacion)
admin.site.register(Tela)