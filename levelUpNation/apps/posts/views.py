from django.shortcuts import render
from .models import Posts

# Vista Basada en Funciones

def posts(request):
    ctx = {}
    noticias = Posts.objects.all()
    ctx["noticias"] = noticias
    return render(request, "posts/index.html", ctx)


def login(request):
    return render(request, "usuarios/login.html")