from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    poster_url = models.URLField(blank=True)
    fecha_lanzamiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class Maraton(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    peliculas = models.ManyToManyField(Pelicula, blank=True)

    def __str__(self):
        return self.nombre
        
    def cantidad_peliculas(self):
        return self.peliculas.count()