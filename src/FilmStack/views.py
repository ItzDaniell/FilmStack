from django.shortcuts import render, redirect, get_object_or_404
from .models import Pelicula, Maraton
from .forms import MaratonForm

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

def lista_maratones(request):
    """Vista para ver la lista de maratones"""
    maratones = Maraton.objects.all()
    return render(request, 'FilmStack/lista_maratones.html', {'maratones': maratones})

def crear_maraton(request):
    """Vista para crear un nuevo maraton"""
    if request.method == 'POST':
        form = MaratonForm(request.POST)
        if form.is_valid():
            maraton = form.save()
            return redirect('agregar_pelicula_maraton', maraton_id=maraton.id)
    else:
        form = MaratonForm()
    
    return render(request, 'FilmStack/form_maraton.html', {'form': form})