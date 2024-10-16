from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Posts, Comentarios
from .form import ComentarioForm


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

def register(request):
    template = loader.get_template("users/register.html")
    return HttpResponse(template.render({}, request))

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
