from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
    path("about/", views.about, name="about"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("contact/", views.contact, name="contact"),
    path("content/<slug:slug_text>/", views.content, name="content"),
    # path("post/<slug:slug_text>/", views.detail, name="detail")
]