from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('archivos/<int:id_tarea>/', views.archivos, name='archivos'),
]