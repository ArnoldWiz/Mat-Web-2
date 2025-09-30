from django.contrib import admin
from .models import Respuesta, Tareas, ArchivoRespuesta

# Register your models here.
admin.site.register(Tareas)
admin.site.register(Respuesta)
admin.site.register(ArchivoRespuesta)
