from django.contrib import admin
from django.urls import path, include, re_path
from Videojuegos.views import inicio, crear_videojuego, listado_videojuegos, acerca_de_nosotros
from post import views

from accounts.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('crear_videojuego', crear_videojuego, name='crear_videojuego'),
    path('listado_videojuegos', listado_videojuegos, name='listado_videojuegos'),
    path('about', acerca_de_nosotros, name='acerca_de_nosotros'),
    path('accounts/', include('accounts.urls')),
    path('crear_post', views.CrearPost.as_view(), name='crear_post'),
    path('listado_posts', views.ListadoPost.as_view(), name='listado_posts'),
    path('mostrar_post/<int:pk>', views.MostrarPost.as_view(), name='mostrar_post'),
    path('editar_post/<int:pk>', views.EditarPost.as_view(), name='editar_post'),
    path('eliminar_post/<int:pk>', views.EliminarPost.as_view(), name='eliminar_post'),
    # re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

