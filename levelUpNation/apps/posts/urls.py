from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.index, name="inicio"),
    path("about/", views.about, name="about"),
     path("register/", views.register.as_view(), name="register"),
    path(
        "login/", LoginView.as_view(template_name="users/login.html"), name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("contact/", views.contact, name="contact"),
    path("content/<slug:slug_text>/", views.content, name="content"),
    # path("post/<slug:slug_text>/", views.detail, name="detail")
]