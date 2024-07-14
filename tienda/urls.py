#from django.conf.urls import url
from django.urls import path
from . import views
from .views import redirigir_whatsapp



urlpatterns = [

    #SECCIÓN PAGINAS------------------------------------------------
    path('joboutique', views.home, name='joboutique'),
    path('pedidos', views.pedidos, name='pedidos'),
    path('donaciones', views.donaciones, name='donaciones'),
    path('carrito', views.carrito, name='carrito'),
    path('registro_login', views.registro, name='registro_login'),
    path('sobremi', views.sobremi, name='sobremi'),
    path('whatsapp/', redirigir_whatsapp, name="redirigir_whatsapp"),
    #SECCIÓN CRUD-----------------------------------------------------
    path('lista_productos', views.lista_productos, name='lista_productos'),
    path('productos_agregar', views.productos_agregar, name='productos_agregar'),
    path('productos_eliminar/<str:pk>', views.productos_eliminar, name='productos_eliminar'),
    path('productos_modificar/<str:pk>/', views.productos_modificar, name='productos_modificar'),
]