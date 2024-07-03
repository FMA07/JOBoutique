#from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('joboutique', views.home, name='joboutique'),
    path('lista_productos', views.lista_productos, name='lista_productos'),
    path('productos_agregar', views.productos_agregar, name='productos_agregar'),
    path('productos_eliminar/<str:pk>', views.productos_eliminar, name='productos_eliminar'),
    path('productos_modificar/<str:pk>/', views.productos_modificar, name='productos_modificar'),
    path('productos_actualizar', views.productos_actualizar, name='productos_actualizar'),
]