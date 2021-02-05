from django.db import models


class Proyectos(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='proyectos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'

    def __str__(self):
        return self.titulo
