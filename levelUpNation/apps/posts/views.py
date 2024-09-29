from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("home.html")
    context = {"title":"Level Up Nation"}
    return HttpResponse(template.render(context, request))

def post(request):
    template = loader.get_template("post.html")
    return HttpResponse(template.render({}, request))