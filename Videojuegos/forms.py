from django import forms

class FormVideojuego(forms.Form):
    nombre = forms.CharField(max_length=50)
    fecha_lanzamiento = forms.DateField(
            widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'})
        )
    genero = forms.CharField(max_length=50)
    valoracion = forms.IntegerField()

class FormBusquedaVideojuego(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)