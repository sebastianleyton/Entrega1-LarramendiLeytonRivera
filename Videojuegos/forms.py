from django import forms

class FormVideojuego(forms.Form):
    nombre = forms.CharField(max_length=50)
    fecha_lanzamiento = forms.DateField()
    genero = forms.CharField(max_length=50)
    valoracion = forms.IntegerField()

class FormBusquedaVideojuego(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)