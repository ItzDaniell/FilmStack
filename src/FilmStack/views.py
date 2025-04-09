from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pelicula, Maraton
from .forms import MaratonForm, AgregarPeliculaForm

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
    """Vista para crear un nuevo examen"""
    if request.method == 'POST':
        form = MaratonForm(request.POST)
        if form.is_valid():
            maraton = form.save()
            messages.success(request, 'Maratón creado correctamente.')
            return redirect('agregar_pelicula_maraton', maraton_id=maraton.id)
    else:
        form = MaratonForm()
    
    return render(request, 'FilmStack/form_maraton.html', {'form': form})

def detalle_maraton(request, maraton_id):
    """Vista para mostrar el detalle de una maratón, incluyendo sus películas."""
    maraton = get_object_or_404(Maraton, id=maraton_id)
    peliculas = maraton.peliculas.all()
    return render(request, 'FilmStack/detalle_maraton.html', {
        'maraton': maraton,
        'peliculas': peliculas,
    })

def actualizar_maraton(request, maraton_id):
    maraton = get_object_or_404(Maraton, id=maraton_id)

    if request.method == 'POST':
        form = MaratonForm(request.POST, instance=maraton)
        if form.is_valid():
            form.save()
            messages.success(request, 'Maratón actualizado correctamente.')
            return redirect('detalle_maraton', maraton_id=maraton.id)
    else:
        form = MaratonForm(instance=maraton)

    return render(request, 'FilmStack/form_maraton.html', {'form': form, 'maraton': maraton})


def eliminar_maraton(request, maraton_id):
    maraton = get_object_or_404(Maraton, id=maraton_id)

    if request.method == 'POST':
        maraton.delete()
        messages.success(request, 'El maratón fue eliminado correctamente.')
        return redirect('lista_maratones')

    return redirect('detalle_maraton', maraton_id=maraton.id)

def agregar_pelicula_maraton(request, maraton_id):
    maraton = get_object_or_404(Maraton, id=maraton_id)

    if request.method == 'POST':
        form = AgregarPeliculaForm(request.POST)
        if form.is_valid():
            pelicula = form.cleaned_data['pelicula']
            maraton.peliculas.add(pelicula)
            messages.success(request, f'Película "{pelicula.titulo}" agregada a la maratón.')
        
        if 'add_another' in request.POST:
            return redirect('agregar_pelicula_maraton', maraton_id=maraton_id)
        elif 'finish' in request.POST:
            return redirect('detalle_maraton', maraton_id=maraton_id)
    else:
        form = AgregarPeliculaForm()

    return render(request, 'FilmStack/agregar_pelicula_maraton.html', {
        'form': form,
        'maraton': maraton,
        'peliculas': maraton.peliculas.all()
    })

def quitar_pelicula_maraton(request, maraton_id, pelicula_id):
    maraton = get_object_or_404(Maraton, id=maraton_id)
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)

    if request.method == 'POST':
        maraton.peliculas.remove(pelicula)
        messages.success(request, f'La película "{pelicula.titulo}" fue eliminada del maratón.')
    
    return redirect('detalle_maraton', maraton_id=maraton_id)