from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from post.models import Post
from .forms import FormBusquedaPost, FormPost


# Create your views here.

class ListadoPost(ListView):
    model = Post
    template_name = 'listado_posts.html'

    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            object_list = self.model.objects.filter(titulo__icontains=titulo)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FormBusquedaPost()
        return context


class CrearPost(CreateView):
    model = Post
    form_class = FormPost
    success_url = '/listado_posts'
    template_name = 'crear_post.html'
    # fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha_creacion']


class EditarPost(UpdateView):
    model = Post
    form_class = FormPost
    success_url = '/listado_posts'
    template_name = 'editar_post.html'
    # fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha_creacion']


class EliminarPost(DeleteView):
    model = Post
    template_name = 'eliminar_post.html'
    success_url = '/listado_posts'


class MostrarPost(DetailView):
    model = Post
    template_name = 'mostrar_post.html'