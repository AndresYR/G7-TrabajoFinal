from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
    path("post/", views.post, name="noticias"),
    path("login/", views.login, name="login")
]