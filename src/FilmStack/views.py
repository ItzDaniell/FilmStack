from django.shortcuts import render, redirect, get_object_or_404
from .models import Pelicula

def lista_peliculas(request):
    """Vista para ver la lista de películas con opción de búsqueda"""
    query = request.GET.get('q', '')
    if query:
        peliculas = Pelicula.objects.filter(titulo__icontains=query)
    else:
        peliculas = Pelicula.objects.all()

    return render(request, 'FilmStack/lista_peliculas.html', {'peliculas': peliculas, 'query': query})

def detalle_pelicula(request, pelicula_id):
    """Vista para mostrar el detalle de una películas"""
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    return render(request, 'FilmStack/detalle_pelicula.html', {'pelicula': pelicula})