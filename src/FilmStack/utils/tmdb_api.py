import requests
from ..models import Pelicula

API_KEY = '345d6a6e1b840869bdbbcee6859a2098'
BASE_URL = 'https://api.themoviedb.org/3'
IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500'

def obtener_peliculas_guardar_en_bd():
    url = f"{BASE_URL}/discover/movie"
    params = {
        'api_key': API_KEY,
        'language': 'es-ES',
        'sort_by': 'popularity.desc',
        'page': 1
    }
    
    todas_las_peliculas = []
    total_peliculas = 120 

    while len(todas_las_peliculas) < total_peliculas:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            peliculas = data.get('results', [])
            todas_las_peliculas.extend(peliculas)

            if len(todas_las_peliculas) >= total_peliculas:
                break

            params['page'] += 1
        else:
            print("Error al obtener datos de la API")
            break

    nuevas_peliculas = []
    for pelicula in todas_las_peliculas[:total_peliculas]:  # Aseguramos que solo obtenemos 120
        poster_url = f"{IMAGE_BASE_URL}{pelicula['poster_path']}" if pelicula.get('poster_path') else None

        pelicula_obj, created = Pelicula.objects.get_or_create(
            titulo=pelicula['title'],
            defaults={
                'descripcion': pelicula.get('overview', ''),
                'poster_url': poster_url,
                'fecha_lanzamiento': pelicula.get('release_date') or None,
            }
        )

        if created:
            nuevas_peliculas.append(pelicula_obj)

    return nuevas_peliculas