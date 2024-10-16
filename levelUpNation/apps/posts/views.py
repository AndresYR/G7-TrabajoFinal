from django.forms import BaseModelForm
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Posts
from django.contrib.auth.models import Group
from django.views.generic import  CreateView


def index(request):
    latest_posts_list = Posts.objects.order_by("-fecha_publicacion")
    template = loader.get_template("home.html")
    context = {"title":"Level Up Nation"}
    if request.POST:
        status = request.POST["categoria"]
        if status != "ALL":
            latest_posts_list = Posts.objects.filter(categoria__nombre=status).order_by("-fecha_publicacion")

        
            
        
    context["latest_posts_list"] = latest_posts_list
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template("about_us.html")
    return HttpResponse(template.render({}, request))

def login(request):
    template = loader.get_template("users/login.html")
    return HttpResponse(template.render({}, request))

def register(request):
    template = loader.get_template("users/register.html")
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template("contact_us.html")
    return HttpResponse(template.render({}, request))

# def content(request):
#     posts = Posts.objects.all()
#     category = Categorias.objects.all()
#     ctx = {'posts': posts,
#            'category': category
#            }
#     template = loader.get_template('posts/posts_content.html')
#     return HttpResponse(template.render(ctx, request))

def content(request, slug_text):
    post = Posts.objects.get(slug=slug_text)
    return render(request, "posts/posts_content.html", {"post":post})
