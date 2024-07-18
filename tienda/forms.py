from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Producto, Donacion, Usuario, Region, Comuna, Ciudad, Tela, Pedido
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

#Formulario de productos
class Productoforms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

#Formulario de donaciones
class Donacionforms(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['email','img_donacion']

    def __init__(self, *args, **kwargs):
        super(Donacionforms, self).__init__(*args, **kwargs)
        self.fields['img_donacion'].label = False
        self.fields['email'].label = False
        self.fields['email'].required = True
        self.helper = FormHelper()
        self.helper.form_class = 'prueba'

#Formulario registro
class Registroforms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Repetir contraseña")
    
    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'appaterno', 'apmaterno', 'region', 'comuna', 'ciudad', 'direccion', 'celular', 'telefono_opcion']
    
    def __init__(self, *args, **kwargs):
        super(Registroforms, self).__init__(*args, **kwargs)
        fields_to_hide = ['email', 'nombre', 'appaterno', 'apmaterno', 'region', 'comuna', 'ciudad', 'direccion', 'celular', 'telefono_opcion', 'password', 'password2']
        for x in fields_to_hide:
            self.fields[x].label = False
        self.fields['comuna'].queryset = Comuna.objects.none()
        self.fields['ciudad'].queryset = Ciudad.objects.none()

        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['comuna'].queryset = Comuna.objects.filter(region_id=region_id).order_by('comuna')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['comuna'].queryset = self.instance.region.comuna_set.order_by('comuna')

        if 'comuna' in self.data:
            try:
                comuna_id = int(self.data.get('comuna'))
                self.fields['ciudad'].queryset = Ciudad.objects.filter(comuna_id=comuna_id).order_by('ciudad')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['ciudad'].queryset = self.instance.comuna.ciudad_set.order_by('ciudad')

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'email',
            'nombre',
            'appaterno',
            'apmaterno',
            'region',
            'comuna',
            'ciudad',
            'direccion',
            'celular',
            'telefono_opcion',
            'password',
            'password2',
            Submit('submit', 'Registrarse')
        )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            self.add_error('password2', "Las contraseñas no coinciden")

        return cleaned_data
    
#Formulario telas
class telaforms(forms.ModelForm):
    class Meta:
        model = Tela
        fields ='__all__'

#Formulario Pedido
class pedidoForms(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['email', 'cod_producto', 'cod_tela', 'descripcion']

        #descripcion_area = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super(pedidoForms, self).__init__(*args, **kwargs)
        self.fields['email'].label= False
        self.fields['cod_tela'].label = False
        self.fields['cod_producto'].label = False
        self.fields['descripcion'].label = False
        self.helper = FormHelper()
        #self.helper.layout = Layout(
        #    'cod_producto',
        #    'cod_tela'
        #    'descripcion_area'
        #)

#Formulario log in

class LoginForm(forms.Form):
    usuario = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Correo Electrónico")
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Contraseña")

    def clean(self):
        usuario = self.cleaned_data.get("usuario")
        contraseña = self.cleaned_data.get("contraseña")
        usuario = authenticate(usuario=usuario, contraseña=contraseña)
        if not usuario:
            raise forms.ValidationError('Correo Electrónico o contraseña incorrectos')
        return self.cleaned_data
