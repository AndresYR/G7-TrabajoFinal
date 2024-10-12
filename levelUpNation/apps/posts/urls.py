from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.index, name="inicio"),
    path("post/", views.post, name="noticias"),
    path("register/", views.register.as_view(), name="register"),
    path(
        "login/", LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("contact/", views.contact, name="contact")
]