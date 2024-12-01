from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Mantenimiento, Vehiculo
from .forms import MantenimientoForm, VehiculoForm

def home(request):
    mantenimientos = Mantenimiento.objects.all()
    return render(request, 'vehiculos/home.html', {'mantenimientos': mantenimientos})


def listar_mantenimientos(request):
    mantenimientos = Mantenimiento.objects.all()
    paginator = Paginator(mantenimientos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'vehiculos/lista_mantenimientos.html', {'page_obj': page_obj})


def crear_mantenimiento(request):
    if request.method == 'POST':
        form = MantenimientoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_mantenimientos')
    else:
        form = MantenimientoForm()
    return render(request, 'vehiculos/crear_mantenimiento.html', {'form': form})

def detalle_mantenimiento(request, mantenimiento_id):
    mantenimiento = get_object_or_404(Mantenimiento, id=mantenimiento_id)
    return render(request, 'vehiculos/detalle_mantenimiento.html', {'mantenimiento': mantenimiento})


def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/crear_vehiculo.html', {'form': form})

def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    paginator = Paginator(vehiculos, 10)  # 10 vehículos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'vehiculos/lista_vehiculos.html', {'page_obj': page_obj})

def detalle_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    return render(request, 'vehiculos/detalle_vehiculo.html', {'vehiculo': vehiculo})

def editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')  # Redirigir al listado después de guardar
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'vehiculos/editar_vehiculo.html', {'form': form, 'vehiculo': vehiculo})

def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('lista_vehiculos')  # Redirigir al listado después de eliminar
    return render(request, 'vehiculos/eliminar_vehiculo.html', {'vehiculo': vehiculo})


def lista_vehiculos_historial(request):
    vehiculos = Vehiculo.objects.prefetch_related('mantenimientos')
    return render(request, 'vehiculos/lista_vehiculos_historial.html', {'vehiculos': vehiculos})


def mantenimientos_recientes(request):
    hoy = date.today()
    seis_meses_atras = hoy - timedelta(days=180)
    mantenimientos = Mantenimiento.objects.filter(fecha__gte=seis_meses_atras).select_related('vehiculo')
    return render(request, 'vehiculos/mantenimientos_recientes.html', {'mantenimientos': mantenimientos})

def estadisticas_mantenimientos(request):
    vehiculos = Vehiculo.objects.annotate(num_mantenimientos=Count('mantenimientos'))
    promedio = Vehiculo.objects.aggregate(promedio_mantenimientos=Avg('mantenimientos__id'))
    return render(request, 'vehiculos/estadisticas_mantenimientos.html', {
        'vehiculos': vehiculos,
        'promedio_mantenimientos': promedio['promedio_mantenimientos']
    })
