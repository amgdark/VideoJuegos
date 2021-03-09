from django import forms
from .models import Categoria, Videojuego


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        fields = '__all__'


class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego

        fields = '__all__'

        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del videojuego','onFocus':'validar(this)'}),
            'anio':forms.NumberInput(attrs={'class':'form-control'}),
            'categoria':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control'}),
        }