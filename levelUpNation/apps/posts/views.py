from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 

from .form import RegistroForm, CrearForm, ModificarForm

from django.shortcuts import render
from .models import Posts, Categorias

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

def post(request):
    template = loader.get_template("posts/post.html")
    return HttpResponse(template.render({}, request))

def login(request):
    template = loader.get_template("users/login.html")
    return HttpResponse(template.render({}, request))

class register(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("noticias")
    template_name = "users/register.html"

""" class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("noticias")
    template_name = "usuarios/registro.html" """

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


class CrearPost(CreateView):
    form_class = CrearForm
    model = Posts
    template_name = "posts/crear_post.html"
    success_url = reverse_lazy("inicio")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)



class EliminarPost(DeleteView):
    model = Posts
    template_name = "posts/posts_confirm_delete.html"
    success_url = reverse_lazy("inicio")


class ModificarPost(UpdateView):
    model = Posts
    form_class = ModificarForm
    template_name = "posts/modificar_post.html"
    success_url = reverse_lazy("inicio")