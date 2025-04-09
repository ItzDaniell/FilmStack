from django.shortcuts import render
from .models import Pelicula

def lista_peliculas(request):
    """Vista para ver la lista de películas con opción de búsqueda"""
    query = request.GET.get('q', '')
    if query:
        peliculas = Pelicula.objects.filter(titulo__icontains=query)
    else:
        peliculas = Pelicula.objects.all()

    return render(request, 'FilmStack/lista_peliculas.html', {'peliculas': peliculas, 'query': query})