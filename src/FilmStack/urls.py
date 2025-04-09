from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_peliculas, name='lista_peliculas'),
    path('FilmStack/<int:pelicula_id>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('FilmStack/maratones/', views.lista_maratones, name='lista_maratones'),
    path('FilmStack/maraton/create', views.crear_maraton, name='crear_maraton'),
    path('FilmStack/maraton/<int:maraton_id>/agregar-pelicula/', views.agregar_pelicula_maraton, name='agregar_pelicula_maraton'),
    path('FilmStack/maraton/<int:maraton_id>/show/', views.detalle_maraton, name='detalle_maraton'),
    path('FilmStack/maraton/<int:maraton_id>/pelicula/<int:pelicula_id>/delete/', views.quitar_pelicula_maraton, name='quitar_pelicula_maraton'),
    path('FilmStack/maraton/<int:maraton_id>/edit/', views.actualizar_maraton, name='editar_maraton'),
    path('FilmStack/maraton/<int:maraton_id>/delete/', views.eliminar_maraton, name='eliminar_maraton'),
]
