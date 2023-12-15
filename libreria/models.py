from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    idioma = models.CharField(max_length=25)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to='portadas/')

