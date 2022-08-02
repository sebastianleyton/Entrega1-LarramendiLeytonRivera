from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class FormPost(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=50)
    # contenido = forms.RichTextField(blank=True, null=True)
    contenido = forms.CharField(widget=CKEditorWidget())
    autor = forms.CharField(max_length=50)
    fecha_creacion = forms.DateField(
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'})
    )


class FormBusquedaPost(forms.Form):
    titulo = forms.CharField(max_length=50, required=False)
