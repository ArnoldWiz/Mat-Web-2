from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/load-municipalities/', views.load_municipalities, name='ajax_load_municipalities'),
]