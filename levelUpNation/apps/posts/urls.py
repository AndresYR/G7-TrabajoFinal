from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
    path("post/", views.post, name="noticias"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("contact/", views.contact, name="contact"),
    path("content/<slug:slug_text>/", views.content, name="content"),
    path("enviarcomentario/<slug:slug_text>", views.enviar_comentario, name="enviar_comentario"),
    path("borrarcomentario/<pk>", views.borrar_comentario, name="borrar_comentario"),
    path("editarcomentario/<pk>", views.editar_comentario, name="editar_comentario")
]