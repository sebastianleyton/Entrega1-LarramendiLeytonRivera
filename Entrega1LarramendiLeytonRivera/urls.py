from django.contrib import admin
from django.urls import path, include
from Videojuegos.views import inicio, crear_videojuego, listado_videojuegos, acerca_de_nosotros
from accounts.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('crear_videojuego', crear_videojuego, name='crear_videojuego'),
    path('listado_videojuegos', listado_videojuegos, name='listado_videojuegos'),
    path('about', acerca_de_nosotros, name='acerca_de_nosotros'),
    path('accounts/', include('accounts.urls'))

]
