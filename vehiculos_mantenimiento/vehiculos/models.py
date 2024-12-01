from django.db import models

class Vehiculo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    año = models.PositiveIntegerField(null=True, blank=True)
    talleres = models.ManyToManyField('Taller', related_name='vehiculos', blank=True)

    def __str__(self):
        return str(self.nombre)


class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='mantenimientos')
    fecha = models.DateField()
    observaciones = models.TextField()
    evidencia_fotografica = models.ImageField(upload_to='evidencias/', blank=True, null=True)
    factura = models.FileField(upload_to='facturas/', blank=True, null=True)

    def __str__(self):
        return f"Mantenimiento de {self.vehiculo.nombre} - {self.fecha}"


class Taller(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
