from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Mantenimiento
from .forms import MantenimientoForm

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
