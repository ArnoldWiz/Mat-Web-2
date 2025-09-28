from django.db import models

class Tareas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_de_entrega = models.DateField()
    prioridad = models.CharField(max_length=50)
    archivo = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Respuesta(models.Model):
    tarea = models.ForeignKey(Tareas, on_delete=models.CASCADE, related_name='respuestas')
    nombre_alumno = models.CharField(max_length=100)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='respuestas/', null=True, blank=True)

    def __str__(self):
        return f"Respuesta de {self.nombre_alumno} para {self.tarea.nombre}"


class ArchivoRespuesta(models.Model):
    respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE, related_name='archivos_adicionales')
    archivo = models.FileField(upload_to='respuestas_archivos/')
    nombre_original = models.CharField(max_length=255)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Archivo {self.nombre_original} de {self.respuesta.nombre_alumno}"
