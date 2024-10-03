from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("home.html")
    context = {"title":"Level Up Nation"}
    return HttpResponse(template.render(context, request))

def post(request):
    template = loader.get_template("post.html")
    return HttpResponse(template.render({}, request))

def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template("contact_us.html")
    return HttpResponse(template.render({}, request))