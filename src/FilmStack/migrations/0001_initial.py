# Generated by Django 3.2.25 on 2025-04-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True)),
                ('poster_url', models.URLField(blank=True)),
                ('fecha_lanzamiento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maraton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('peliculas', models.ManyToManyField(blank=True, to='FilmStack.Pelicula')),
            ],
        ),
    ]
