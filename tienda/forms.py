from django import forms
from .models import Producto

class Productoforms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"