from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 

from .form import RegistroForm, CrearForm, ModificarForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Posts, Comentarios
from .form import ComentarioForm, RegistroForm
from django.contrib.auth.models import Group, Permission



def index(request):
    latest_posts_list = Posts.objects.order_by("-fecha_publicacion")
    template = loader.get_template("home.html")
    context = {"title":"Level Up Nation"}
    
    if request.GET:
        status = request.GET["filtro"]
        if status == "Alfabeto":
            latest_posts_list = Posts.objects.order_by("-titulo")
        elif status == "Autor":
            autor = request.user
            if autor:
                latest_posts_list = Posts.objects.filter(autor__username=autor).order_by("-fecha_publicacion")
            
            
    
    # Filtro por categoria
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


def content(request, slug_text):
    post = Posts.objects.get(slug=slug_text)
    
    form_comentario = ComentarioForm()
    
    context = {
        "post" : post,
        "form_comentario" : form_comentario
    }
    
    return render(request, "posts/posts_content.html", context)


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
    
def enviar_comentario(request, slug_text):
    post = Posts.objects.get(slug=slug_text)
    
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        
        if form.is_valid:
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.post = post
            comentario.save()
    
    return redirect("content", post.slug)


def borrar_comentario(request, pk):
    comentario = get_object_or_404(Comentarios, id=pk, autor=request.user)
    
    if request.method == "POST":
        comentario.delete()
        messages.success(request, "Comentario borrado")
        return redirect("content", comentario.post.slug)
    
    return render(request, "comentarios/delete_comment.html", {"comentario":comentario})

def editar_comentario(request, pk):
    comentario = get_object_or_404(Comentarios, id=pk)
    context = {}    
    
    form = ComentarioForm(instance=comentario)

    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect("content", comentario.post.slug)
        
    context["form_comentario"] = form
    
    return render(request, "comentarios/update_comment.html", context)



class RegistrarUsuario(CreateView):
    template_name = 'users/register.html'
    form_class = RegistroForm

    def form_valid(self, form):
        response = super().form_valid(form)
        group = Group.objects.get(name='Registrado')
        self.object.groups.add(group)
        return redirect('apps.users:register')