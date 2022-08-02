from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    # contenido = RichTextUploadingField(blank=True, null=True)
    contenido = RichTextField(blank=True, null=True)
    # autor = models.CharField(max_length=50)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField()
    # imagen = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)