from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
    path("post/", views.post, name="noticias"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("contact/", views.contact, name="contact"),
    path("content/", views.content, name="content"),
    #crea un nuevo post
    path("nuevo_post/", views.CrearPosts.as_view(), name="nuevo_post"),
    #eliminar
    path("eliminar/<int:pk>", views.EliminarPost.as_view(), name="eliminar_post"),
    #modificar
    path("modificar/<int:pk>", views.EliminarPost.as_view(), name="modificar_post"),
    # perfil del usuario
    #path("perfil/<int:id>", views.perfil, name="eliminar_post"),
    #url de comentario
    #path("comentar/", views.comentar_post, name="comentar"),
]