from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
    path("post/", views.post, name="noticias"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("contact/", views.contact, name="contact"),
    path("content/", views.content, name="content")
]