from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Tareas

# Create your views here.

def index(request):
    return render(request, 'app/index.html', {'tareas': Tareas.objects.all()})

def archivos(request, id_tarea):
    tarea = Tareas.objects.get(id=id_tarea)
    return render(request, 'app/archivos.html', {'tarea': tarea})