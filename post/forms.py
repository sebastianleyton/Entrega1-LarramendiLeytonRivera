from django import forms

class FormBusquedaPost(forms.Form):
    titulo = forms.CharField(max_length=50, required=False)
