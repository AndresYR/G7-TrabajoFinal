from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save

from .utils import set_slug
import uuid

class User(AbstractUser):
    icono = models.ImageField(upload_to="media/usuarios", null=True, blank=True)
    descripcion = models.TextField(max_length=350)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
    
class Categorias(models.Model):
    nombre = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "Categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Posts(models.Model):
    titulo = models.CharField(max_length=250, verbose_name="Titulo")
    contenido = models.TextField(verbose_name="Contenido")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="posts", null=True, blank=True)
    slug = models.SlugField(max_length=200, null=False, blank=True, editable=False)
   
    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = "Post"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

# Genera un url en forma automatica
pre_save.connect(set_slug, sender= Posts)      

class Comentarios(models.Model):
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comments")
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="comments")
    contenido = models.TextField(max_length=150, verbose_name="Contenido")
    fecha = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f"{self.autor.username} : {self.contenido[:30]}"
        except:
            return f"sin autor : {self.contenido[:30]}"

    class Meta:
        ordering = ["-fecha"]
        db_table = "Comentarios"

