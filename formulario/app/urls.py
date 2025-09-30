from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('tarea/<int:tarea_id>/responder/', views.responder_tarea, name='responder_tarea'),
    path('tarea/<int:tarea_id>/respuestas/', views.ver_respuestas, name='ver_respuestas'),
]
