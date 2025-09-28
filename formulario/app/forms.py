from django import forms
from .models import Respuesta

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['nombre_alumno', 'descripcion']
        widgets = {
            'nombre_alumno': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
