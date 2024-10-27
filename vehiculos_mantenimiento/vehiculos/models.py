from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='fotos/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nombre)

