from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Tela, Donacion, Ciudad, Comuna
from .forms import Productoforms, Donacionforms, Registroforms
from django.http import HttpResponseRedirect, JsonResponse

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
    data = {'form': Donacionforms()}
    if request.method == 'POST':
        formulario = Donacionforms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Donacion realizada"
            return redirect(to='donaciones')
        else:
            data['form'] = formulario
    return render(request, 'tienda/donaciones.html', data)

def carrito(request):
    return render(request, 'tienda/cart.html')

def sobremi(request):
    return render(request, 'tienda/sobreMi.html')

def registro(request):
    data = {'form': Registroforms()}
    if request.method == 'POST':
        formulario = Registroforms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            usuario = formulario.save(commit = False)
            usuario.contraseña = formulario.cleaned_data['password']
            usuario.save()
            data["mensaje"] = "Registrado con éxito"
            return redirect(to='home')
        else:
            data['form'] = formulario
    return render(request, 'tienda/registrarse.html', data)
#SECCIÓN FUNCIONALIDAD SELECCION CIUDADES---------------------------------------------

def cargar_comunas(request):
    region_id = request.GET.get('region')
    comunas = Comuna.objects.filter(region_id=region_id).all()
    return JsonResponse(list(comunas.values('id', 'comuna')), safe=False)

def cargar_ciudades(request):
    comuna_id = request.GET.get('comuna')
    ciudades = Ciudad.objects.filter(comuna_id=comuna_id).all()
    return JsonResponse(list(ciudades.values('id','ciudad')), safe=False)

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

