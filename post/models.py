from datetime import date
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    contenido = RichTextField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(default=date.today)
    imagen = models.ImageField(upload_to="imagenes_de_posts/")

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('mostrar_post', args=(str(self.id)))
