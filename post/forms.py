from django import forms
from .models import Post

class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'contenido', 'autor', 'fecha_creacion', 'imagen')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control'}),
        }




class FormBusquedaPost(forms.Form):
    titulo = forms.CharField(max_length=50, required=False)
