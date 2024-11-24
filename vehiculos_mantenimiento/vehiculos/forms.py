from django import forms
from .models import Mantenimiento, Vehiculo #lo van a llamar como llamaron a su modelo
from datetime import date

#Definimos la clase formulario.
class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields= ['vehiculo', 'fecha','observaciones', 'evidencia_fotografica', 'factura']

    #Validacion para el campo de fecha
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha > date.today():
            raise forms.ValidationError("La fecha del mantenimiento no puede ser en el futuro.")
        return fecha

    #hacemos una validacion para el campo observaciones.
    def clean_observaciones(self):
        observaciones = self.cleaned_data.get('observaciones')
        if len(observaciones) < 10:
            raise forms.ValidationError('Las observaciones deben tener al menos 10 caracteres.')
        return observaciones

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['nombre', 'tipo', 'año']
