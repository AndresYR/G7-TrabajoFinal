from django.http import HttpResponse
from django.template import loader

from .models import Posts

def index(request):
    latest_posts_list = Posts.objects.order_by("-fecha_publicacion")
    template = loader.get_template("home.html")
    context = {"title":"Level Up Nation"}
    context["latest_posts_list"] = latest_posts_list
    return HttpResponse(template.render(context, request))

def post(request):
    template = loader.get_template("post.html")
    return HttpResponse(template.render({}, request))

def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render({}, request))

def register(request):
    template = loader.get_template("register.html")
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template("contact_us.html")
    return HttpResponse(template.render({}, request))