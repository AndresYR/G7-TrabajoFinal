from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView
from django.urls import reverse_lazy 
from django.shortcuts import redirect
from .form import RegistroForm
from django.shortcuts import render
from .models import Posts
from django.contrib.auth.models import Group, Permission


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

class register(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("inicio")
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




class RegistrarUsuario(CreateView):
    template_name = 'users/register.html'
    form_class = RegistroForm

    def form_valid(self, form):
        response = super().form_valid(form)
        group = Group.objects.get(name='Registrado')
        self.object.groups.add(group)
        return redirect('apps.users:register')