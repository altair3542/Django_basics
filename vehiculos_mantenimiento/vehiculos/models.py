import os
from django.db import models
from PIL import Image

def ruta_evidencias(instance, filename):
    # Ruta dinámica para las imágenes de evidencia
    return f"evidencias/vehiculo_{instance.vehiculo.id}/{filename}"

def ruta_facturas(instance, filename):
    # Ruta dinámica para las facturas en PDF
    return f"facturas/mantenimiento_{instance.id}/{filename}"

class Vehiculo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    año = models.PositiveIntegerField(null=True, blank=True)
    talleres = models.ManyToManyField('Taller', related_name='vehiculos', blank=True)

    def __str__(self):
        return str(self.nombre)

import os
from PIL import Image
from django.conf import settings

def ruta_evidencias(instance, filename):
    return f"evidencias/vehiculo_{instance.vehiculo.id}/{filename}"

def ruta_facturas(instance, filename):
    return f"facturas/mantenimiento_{instance.id}/{filename}"

class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, related_name='mantenimientos')
    fecha = models.DateField()
    observaciones = models.TextField()
    evidencia_fotografica = models.ImageField(upload_to=ruta_evidencias, blank=True, null=True)
    miniatura = models.ImageField(upload_to='miniaturas/', blank=True, null=True)
    factura = models.FileField(upload_to=ruta_facturas, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.evidencia_fotografica:
            # Crear la ruta de la miniatura
            miniatura_ruta = self.evidencia_fotografica.path.replace('evidencias', 'miniaturas')

            # Crear directorio si no existe
            miniatura_directorio = os.path.dirname(miniatura_ruta)
            if not os.path.exists(miniatura_directorio):
                os.makedirs(miniatura_directorio)

            # Crear miniatura
            imagen = Image.open(self.evidencia_fotografica.path)
            imagen.thumbnail((200, 200))  # Tamaño máximo
            imagen.save(miniatura_ruta)

            # Guardar la ruta de la miniatura
            self.miniatura = miniatura_ruta.replace(settings.MEDIA_ROOT, '')
            super().save(*args, **kwargs)




class Taller(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
