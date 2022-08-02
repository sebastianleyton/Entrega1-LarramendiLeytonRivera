from django.contrib import admin
from django.urls import path, include, re_path
from Videojuegos.views import inicio, crear_videojuego, listado_videojuegos, acerca_de_nosotros
from post.views import crear_post, listado_posts, DetallePost
from accounts.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('crear_videojuego', crear_videojuego, name='crear_videojuego'),
    path('listado_videojuegos', listado_videojuegos, name='listado_videojuegos'),
    path('about', acerca_de_nosotros, name='acerca_de_nosotros'),
    path('accounts/', include('accounts.urls')),
    path('crear_post', crear_post, name='crear_post'),
    path('listado_posts', listado_posts, name='listado_posts'),
    path('detalle_post/<int:pk>', DetallePost.as_view(), name='detalle_post'),
    # re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]
