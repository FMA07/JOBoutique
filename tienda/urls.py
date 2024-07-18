#from django.conf.urls import url
from django.urls import path
from . import views
from .views import redirigir_whatsapp, login, redirigir_insta



urlpatterns = [

#SECCIÓN PAGINAS------------------------------------------------
    path('joboutique', views.home, name='joboutique'),
    path('pedidos', views.pedidos, name='pedidos'),
    path('donaciones', views.donaciones, name='donaciones'),
    path('carrito', views.carrito, name='carrito'),
    path('registro', views.registro, name='registro'),
    path('ajax/cargar_comunas/', views.cargar_comunas, name='cargar_comunas'),
    path('ajax/cargar_ciudades/', views.cargar_ciudades, name='cargar_ciudades'),
    path('sobremi', views.sobremi, name='sobremi'),
    path('whatsapp/', redirigir_whatsapp, name="redirigir_whatsapp"),
    path('instagram/', redirigir_insta, name="redirigir_insta"),
    path('gestor_admin', views.gestor_admin, name='gestor_admin'),
    path('login/', views.login, name='login'),
#SECCIÓN CRUD-----------------------------------------------------
    #Producto--------------------------
    path('lista_productos', views.lista_productos, name='lista_productos'),
    path('productos_agregar', views.productos_agregar, name='productos_agregar'),
    path('productos_eliminar/<str:pk>', views.productos_eliminar, name='productos_eliminar'),
    path('productos_modificar/<str:pk>/', views.productos_modificar, name='productos_modificar'),
    #Tela------------------------------
    path('lista_telas/',views.lista_telas, name = 'lista_telas'),
    path('agregar_telas',views.agregar_telas, name = 'agregar_telas'),
    path('modificar_telas/<str:pk>/',views.modificar_telas, name = 'modificar_telas'),
    path('eliminar_telas/<str:pk>/',views.eliminar_telas, name = 'eliminar_telas'),
    #Pedido--------------------------
    path('lista_pedidos/',views.lista_pedidos, name = 'lista_pedidos'),
    path('eliminar_pedidos/<str:pk>/',views.eliminar_pedidos, name = 'eliminar_pedidos'),
    #Donacion
    path('lista_donaciones/',views.lista_donaciones, name = 'lista_donaciones'),
    path('eliminar_donaciones/<str:pk>/',views.eliminar_donaciones, name = 'eliminar_donaciones'),
]