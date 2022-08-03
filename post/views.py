from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from post.models import Post
from .forms import FormBusquedaPost, FormPost
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


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

def inicio(request):

    ultimos_diez_posts = Post.objects.all().order_by('-id')[:10]

    return render(request, 'index.html', {'listado_posts': ultimos_diez_posts[:3], 'ultimos_diez': ultimos_diez_posts})


def acerca_de_nosotros(request):
    return render(request, 'about.html')

class CrearPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = FormPost
    success_url = '/listado_posts'
    template_name = 'crear_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditarPost(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = FormPost
    success_url = '/listado_posts'
    template_name = 'editar_post.html'


class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'eliminar_post.html'
    success_url = '/listado_posts'


class MostrarPost(DetailView):
    model = Post
    template_name = 'mostrar_post.html'