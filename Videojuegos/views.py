from django.shortcuts import render, redirect
from Videojuegos.models import Videojuego
from .forms import FormVideojuego, FormBusquedaVideojuego


def inicio(request):
    return render(request, 'index.html')


def acerca_de_nosotros(request):
    return render(request, 'about.html')


def crear_videojuego(request):
    form = FormVideojuego(request.POST)

    if form.is_valid():
        data = form.cleaned_data

        videojuego = Videojuego(
            nombre=data.get('nombre'),
            fecha_lanzamiento=data.get('fecha_lanzamiento'),
            genero=data.get('genero'),
            valoracion=data.get('valoracion')
        )
        videojuego.save()

        return redirect('listado_videojuegos')

    else:
        return render(request, 'crear_videojuego.html', {'form': form})


def listado_videojuegos(request):
    nombre_de_busqueda = request.GET.get('nombre')

    if nombre_de_busqueda:
        listado_videojuegos = Videojuego.objects.filter(nombre__icontains=nombre_de_busqueda)
    else:
        listado_videojuegos = Videojuego.objects.all()

    form = FormBusquedaVideojuego()
    return render(request, 'listado_videojuegos.html', {'listado_videojuegos': listado_videojuegos, 'form': form})
