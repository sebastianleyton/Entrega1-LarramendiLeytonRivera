from django.contrib import admin
from django.urls import path, include, re_path
from Videojuegos.views import crear_videojuego, listado_videojuegos
from post import views as pviews
from mensajeria import views
from django.conf import settings
from django.conf.urls.static import static
from post.views import inicio, acerca_de_nosotros

from accounts.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('crear_videojuego', crear_videojuego, name='crear_videojuego'),
    path('listado_videojuegos', listado_videojuegos, name='listado_videojuegos'),
    path('about', acerca_de_nosotros, name='acerca_de_nosotros'),
    path('accounts/', include('accounts.urls')),
    path('crear_post', pviews.CrearPost.as_view(), name='crear_post'),
    path('listado_posts', pviews.ListadoPost.as_view(), name='listado_posts'),
    path('mostrar_post/<int:pk>', pviews.MostrarPost.as_view(), name='mostrar_post'),
    path('editar_post/<int:pk>', pviews.EditarPost.as_view(), name='editar_post'),
    path('eliminar_post/<int:pk>', pviews.EliminarPost.as_view(), name='eliminar_post'),
    path('enviar_mensaje', views.EnviarMensaje.as_view(), name='enviar_mensaje'),
    path('listado_mensajes', views.ListadoMensaje.as_view(), name='listado_mensajes'),
    path('mostrar_mensaje/<int:pk>', views.MostrarMensaje.as_view(), name='mostrar_mensaje'),
    path('eliminar_mensaje/<int:pk>', views.EliminarMensaje.as_view(), name='eliminar_mensaje'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

