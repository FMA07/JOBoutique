from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Tela, Donacion, Ciudad, Comuna, Pedido
from .forms import Productoforms, Donacionforms, Registroforms, telaforms, pedidoForms, LoginForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth import login, authenticate

# Create your views here.

#REDIRECCION PAGINAS EXTERNAS
def redirigir_whatsapp(request):
    return HttpResponseRedirect('https://wa.me/56973317862')
def redirigir_insta(request):
    return HttpResponseRedirect('https://www.instagram.com/creaciones_jo_boutique?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==')

#VISTAS DE PÁGINAS-----------------------------------------------------------

def home(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, 'tienda/home.html', context)

def pedidos(request):
    telas = Tela.objects.all()
    context = {"telas": telas}
    if request.method == 'POST':
        formulario = pedidoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            context["mensaje"] = "Pedido realizado"
            return redirect(to='pedidos')
        else:
            context['form'] = formulario
    else:
        context['form'] = pedidoForms()
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

def gestor_admin(request):
    return render(request, 'tienda/gestor_admin.html')    

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
#telas-------------------------------------------------------------------
def lista_telas(request):
    telas = Tela.objects.all()
    context = {"telas": telas}
    return render(request,'tienda/telas/lista_telas.html',context)

def agregar_telas(request):
    data = {'form': telaforms()}
    if request.method == 'POST':
        formulario = telaforms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Tela agregado"
            return redirect(to='lista_telas')
        else:
            data['form'] = formulario
    return render(request, 'tienda/telas/agregar_telas.html', data)
    
def modificar_telas(request, pk):
    tela = get_object_or_404(Tela, cod_tela=pk)
    data = {'form': telaforms(instance=tela)}
    if request.method == 'POST':
        formulario = telaforms(data=request.POST, instance= tela, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Tela actualizada"
            return redirect(to='lista_telas')
    return render(request, 'tienda/telas/modificar_telas.html', data)

def eliminar_telas(request, pk):
    tela = get_object_or_404(Tela, cod_tela=pk)
    tela.delete()
    return redirect(to='lista_telas')

#Productos-------------------------------------------------------------------
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
        
#Pedidos--------------------------------------------------------------------------------------    
def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    context = {"pedidos": pedidos}
    return render(request, 'tienda/pedidos/lista_pedidos.html', context)
def eliminar_pedidos(request, pk):
    pedido = get_object_or_404(Pedido, cod_pedido=pk)
    pedido.delete()
    return redirect(to='lista_pedidos')
#Donaciones
def lista_donaciones(request):
    donaciones = Donacion.objects.all()
    context = {"donaciones": donaciones}
    return render(request, 'tienda/donaciones/lista_donaciones.html', context)
def eliminar_donaciones(request, pk):
    donacion = get_object_or_404(Donacion, id_donacion=pk)
    donacion.delete()
    return redirect(to='lista_donaciones')   
#SECCION AGREGAR USUARIOS----------------------------------------------------------------

def registro(request):
    data = {'form': Registroforms()}
    if request.method == 'POST':
        formulario = Registroforms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            usuario = formulario.save(commit = False)
            usuario.contraseña = formulario.cleaned_data['password']
            usuario.save()
            data["mensaje"] = "Registrado con éxito"
            return redirect(to='joboutique')
        else:
            data['form'] = formulario
    return render(request, 'tienda/registrarse.html', data)

#SECCION LOGIN----------------------------------------------------------------------------
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usuario = authenticate(usuario=usuario, password=password)
            if usuario is not None:
                login(request, usuario)

                return redirect('home')

    else:

        form = LoginForm()

    return render(request, 'login.html', {'form': form})