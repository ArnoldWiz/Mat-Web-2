from django.shortcuts import render, get_object_or_404, redirect
from .models import Tareas, Respuesta, ArchivoRespuesta
from .forms import RespuestaForm

def lista_tareas(request):
    tareas = Tareas.objects.all()
    return render(request, 'app/index.html', {'tareas': tareas})

def responder_tarea(request, tarea_id):
    tarea = get_object_or_404(Tareas, pk=tarea_id)
    if request.method == 'POST':
        form = RespuestaForm(request.POST, request.FILES)
        if form.is_valid():
            archivos = request.FILES.getlist('archivos')
            errores = []
            allowed_types = ['application/pdf', 'image/jpeg', 'image/png']
            allowed_ext = ['pdf', 'jpg', 'jpeg', 'png']
            max_size = 10 * 1024 * 1024  # 10MB

            for f in archivos:
                ext = f.name.split('.')[-1].lower() if '.' in f.name else ''
                if f.content_type not in allowed_types and ext not in allowed_ext:
                    errores.append(f"El archivo '{f.name}' no es válido. Solo PDF, JPG o PNG.")
                if f.size > max_size:
                    errores.append(f"El archivo '{f.name}' es demasiado grande. Máximo 10MB.")

            if errores:
                for err in errores:
                    form.add_error(None, err)
            else:
                respuesta = form.save(commit=False)
                respuesta.tarea = tarea
                respuesta.save()
                
                for f in archivos:
                    ArchivoRespuesta.objects.create(
                        respuesta=respuesta,
                        archivo=f,
                        nombre_original=f.name
                    )

                return redirect('ver_respuestas', tarea_id=tarea.id)
    else:
        form = RespuestaForm()
    return render(request, 'app/responder.html', {'form': form, 'tarea': tarea})

def ver_respuestas(request, tarea_id):
    tarea = get_object_or_404(Tareas, pk=tarea_id)
    respuestas = tarea.respuestas.all()
    return render(request, 'app/respuestas.html', {'tarea': tarea, 'respuestas': respuestas})
