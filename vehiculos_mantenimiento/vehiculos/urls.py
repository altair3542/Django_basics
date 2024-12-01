from django.urls import path
from . import views

urlpatterns = [
    # una vista para el home
    path('', views.home, name='home'),
    # ruta para crear un nuevo mantenimiento
    path('crear/', views.crear_mantenimiento, name='crear_mantenimiento'),
    # ver todos los mantenimientos
    path('mantenimientos/', views.listar_mantenimientos, name='lista_mantenimientos'),
    # ver un mantenimiento especifico
    path('mantenimientos/<int:mantenimiento_id>/', views.detalle_mantenimiento, name='detalle_mantenimiento'),
    # ruta para crear vehiculos
    path('vehiculos/crear/', views.crear_vehiculo, name='crear_vehiculo'),
    # ver todos los vehiculos
    path('vehiculos/', views.listar_vehiculos, name='lista_vehiculos'),
    # ver un vehiculo individual
    path('vehiculos/<int:vehiculo_id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    # editar un vehiculo especifico
    path('vehiculos/<int:vehiculo_id>/editar/', views.editar_vehiculo, name='editar_vehiculo'),
    # eliminar un vehiculo especifico
    path('vehiculos/<int:vehiculo_id>/eliminar/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    # verificar un historial de vehiculos
    path('vehiculos/historial/', views.lista_vehiculos_historial, name='lista_vehiculos_historial'),
    # ver mantenimientos recientes
    path('mantenimientos/recientes/', views.mantenimientos_recientes, name='mantenimientos_recientes'),
    # ver estadisticas de mantenimientos
    path('estadisticas/', views.estadisticas_mantenimientos, name='estadisticas_mantenimientos'),
]
