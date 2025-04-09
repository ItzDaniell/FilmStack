from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_peliculas, name="lista_peliculas"),
    path('FilmStack/<int:pelicula_id>/', views.detalle_pelicula, name='detalle_pelicula'),
]
