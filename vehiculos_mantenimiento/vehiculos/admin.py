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

    def miniatura_vista(self, obj):
        if obj.miniatura:
            return format_html('<img src="{}" style="width:50px; height:50px;">', obj.miniatura.url)
        return "No disponible"
    miniatura_vista.short_desvription = "Miniatura"




# Register your models here.
# admin.site.register(Vehiculo)
# admin.site.register(Mantenimiento, MantenimientoAdmin)
