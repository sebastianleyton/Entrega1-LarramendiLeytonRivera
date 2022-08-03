# Entrega1-LarramendiLeytonRivera
Miembros: Marcio Larramendi, Sebastian Leyton, Juan Manuel Rivera

El primer paso para lanzar el servidor es crear la base de datos utilizando los comandos


*python manage.py migrate*

*python manage.py makemigrations*

Para lanzar el servidor web se debe ejecutar el comando

*python manage.py runserver*

Levantado el sitio se debe entrar a la URL generada en la terminal, usualmente es http://127.0.0.1:8000/
 
Dentro del sitio se pueden ver posts publicados. En caso de que los haya.

Funcionalidades

Usuarios

    Registro
    Login
    Avatar
    Cambio de contraseña

Posts

    Publicar
    Editar
    Eliminar


Mensajería

    Enviar mensaje
    Leer mensajes   
    

Inicialmente se necesitará crear un usuario (o varios para testear mensajería)
Luego de loguearse, podremos ir a 'Crear post' para crear publicaciones en el blog.
Para crear una publicación se tienen que llenar todos los campos (incluida la imagen)

En la página principal se puede ver un preview de las ultimas 3 publicaciones, 
ademas del titulo de las ultimas 10 publicaciones.

En la ventana 'listado de posts' se pueden ver todos los posts en el blog, buscar por titulo
y si el usuario logueado es el creador, podrá editar y eliminar publicaciones.


En 'mensajes' se pueden leer los mensajes recibidos así como también enviar mensajes a otros usuarios