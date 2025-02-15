from django.db import models

class Proyectos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, default='Sin descripción')  # Valor por defecto
    git = models.URLField(max_length=255, blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)  # Carpeta "proyectos/"

    def __str__(self):
        return self.nombre
