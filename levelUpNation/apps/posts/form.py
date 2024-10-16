from django import forms
from .models import Comentarios

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ["contenido"]
        widgets = {
            "contenido" : forms.TextInput(attrs={"placeholder": "Agregar comentario ...",
                                                 "class" : "area-comentario"})
        }
        labels = {
            "contenido" : ""
        }