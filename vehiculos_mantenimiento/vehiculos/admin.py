from django.contrib import admin
from .models import Vehiculo, Mantenimiento, Taller

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'año')
    search_fields = ('nombre', 'tipo')
    filter_horizontal = ('talleres',)

@admin.register(Taller)
class TallerAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'fecha', 'observaciones')
    list_filter = ('fecha',)


# Register your models here.
# admin.site.register(Vehiculo)
# admin.site.register(Mantenimiento, MantenimientoAdmin)
