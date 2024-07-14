from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Tela, Donacion
from .forms import Productoforms, Donacionforms
from django.http import HttpResponseRedirect

# Create your views here.

#REDIRECCION PAGINAS EXTERNAS
def redirigir_whatsapp(request):
    return HttpResponseRedirect('https://wa.me/qr/HUUEM6JLE72RD1')

#VISTAS DE PÁGINAS-----------------------------------------------------------

def home(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, 'tienda/home.html', context)

def pedidos(request):
    telas = Tela.objects.all()
    context = {"telas": telas}
    return render(request, 'tienda/pedidos.html', context)

def donaciones(request):
    if request.method == 'POST':
        formulario = Donacionforms(request.POST, request.FILES)
    return render(request, 'tienda/donaciones.html', data)

def carrito(request):
    return render(request, 'tienda/cart.html')

def registro(request):
    return render(request, 'tienda/registroLogin.html')

def sobremi(request):
    return render(request, 'tienda/sobreMi.html')

#SECCIÓN CRUD----------------------------------------------------------------

def lista_productos(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, 'tienda/productos/lista_productos.html', context)

def productos_agregar(request):
    data = {'form': Productoforms()}
    if request.method == 'POST':
        formulario = Productoforms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto agregado"
            return redirect(to='lista_productos')
        else:
            data['form'] = formulario
    return render(request, 'tienda/productos/productos_agregar.html', data)
    
def productos_eliminar(request, pk):
    producto = get_object_or_404(Producto, cod_producto=pk)
    producto.delete()
    return redirect(to='lista_productos')
    
def productos_modificar(request, pk):
    producto = get_object_or_404(Producto, cod_producto=pk)
    data = {'form': Productoforms(instance=producto)}
    if request.method == 'POST':
        formulario = Productoforms(data=request.POST, instance= producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto actualizado"
            return redirect(to='lista_productos')
    return render(request, 'tienda/productos/productos_modificar.html', data)
        

#SECCION AGREGAR USUARIOS----------------------------------------------------------------

