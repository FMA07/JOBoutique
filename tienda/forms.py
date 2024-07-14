from django import forms
from .models import Producto, Donacion
from django.contrib.auth.forms import UserCreationForm

#Formulario de productos
class Productoforms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

#Formulario de donaciones
class Donacionforms(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['img_donacion']

class CreacionUsuario(UserCreationForm):
    pass