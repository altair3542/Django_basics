from django.urls import path
from . import views

urlpatterns = [
    # ruta para crear un nuevo mantenimiento
    path('crear/', views.crear_mantenimiento, name='crear_mantenimiento'),
    # ver todos los mantenimientos
    path('', views.listar_mantenimientos, name='lista_mantenimientos'),
]
