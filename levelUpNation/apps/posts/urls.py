from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.index, name="inicio"),
    path("about/", views.about, name="about"),
    path("register/", views.Register.as_view(), name="register"),
    path(
        "login/", LoginView.as_view(template_name="users/login.html"), name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("contact/", views.contact, name="contact"),
    #crea un nuevo post
    path("nuevo_post/", views.CrearPost.as_view(), name="nuevo_post"),
    #eliminar
    path("eliminar/<int:pk>", views.EliminarPost.as_view(), name="eliminar_post"),
    #modificar
    path("modificar/<int:pk>", views.ModificarPost.as_view(), name="modificar_post"),
    # perfil del usuario
    #path("perfil/<int:id>", views.perfil, name="eliminar_post"),
    #url de comentario
    #path("comentar/", views.comentar_post, name="comentar"),
    path("content/<slug:slug_text>/", views.content, name="content"),
    path("enviarcomentario/<slug:slug_text>", views.enviar_comentario, name="enviar_comentario"),
    path("borrarcomentario/<pk>", views.borrar_comentario, name="borrar_comentario"),
    path("editarcomentario/<pk>", views.editar_comentario, name="editar_comentario")
]