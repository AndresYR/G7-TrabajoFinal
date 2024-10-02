from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="noticias"),
    path("post/", views.post, name="post"),
    path("login/", views.login, name="login")
]