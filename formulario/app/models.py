from django.db import models

# Create your models here.

class Tareas (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_de_entrega = models.DateField()
    prioridad = models.CharField(max_length=50)
    archivo = models.BooleanField(default=False)