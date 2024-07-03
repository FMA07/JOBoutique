from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import Productoforms

# Create your views here.



def home(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, 'tienda/home.html', context)

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
        
def productos_actualizar(request):

    if request.method == "POST":
        codigo = request.POST.get("codigo")
        nombre=request.POST["nombre"]
        precio=request.POST["precio"]
        cantidad=request.POST["cantidad"]
        descripcion=request.POST["descripcion"]
        imagen=request.POST["imagen"]

        producto = get_object_or_404(Producto, cod_producto=codigo)
        producto.nombre=nombre
        producto.precio=precio
        producto.cantidad=cantidad
        producto.descripcion=descripcion
        producto.img_producto=imagen
        producto.save()

        context={'mensaje':'Datos actualizados'}
        return render(request, 'tienda/productos/productos_modificar.html', context)

    else:
        productos = Producto.objects.all()
        context = {'productos': productos}
        return render(request, 'tienda/productos/lista_productos.html', context)
        