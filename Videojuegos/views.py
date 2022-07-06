from django.shortcuts import render
from Videojuegos.models import Videojuego


def inicio(request):
    videojuego_1 = Videojuego(nombre='Camellosaurio Ninja', fecha_lanzamiento='26/06/2021',genero='Aventura',valoracion=98)
    return render(request, 'index.html', {'videojuego':videojuego_1})