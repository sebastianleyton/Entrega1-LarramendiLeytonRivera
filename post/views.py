from django.shortcuts import render, redirect
from django.views.generic import DetailView

from post.models import Post
from .forms import FormPost, FormBusquedaPost


# Create your views here.

def crear_post(request):
    form = FormPost(request.POST)

    if form.is_valid():
        data = form.cleaned_data

        post = Post(
            titulo=data.get('titulo'),
            subtitulo=data.get('subtitulo'),
            contenido=data.get('contenido'),
            autor=data.get('autor'),
            fecha_creacion=data.get('fecha_creacion'),
        )
        post.save()

        return redirect('listado_posts')

    else:
        return render(request, 'crear_post.html', {'form': form})

def listado_posts(request):
    titulo_de_busqueda = request.GET.get('titulo')

    if titulo_de_busqueda:
        listado_posts = Post.objects.filter(titulo__icontains=titulo_de_busqueda)
    else:
        listado_posts = Post.objects.all()

    form = FormBusquedaPost()
    return render(request, 'listado_posts.html', {'listado_posts': listado_posts, 'form': form})

class DetallePost(DetailView):
    model = Post
    template_name = 'detalle_post.html'

