from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save

from .utils import set_slug

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
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(max_length=250, verbose_name="Contenido")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)



#class Imagenes(models.Model):
#    imagen = models.ImageField(upload_to="/media/posts")
#    post = models.ForeignKey(Posts, on_delete=models.CASCADE)