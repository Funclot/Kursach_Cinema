from django.shortcuts import render
from .models import Movie


def movie_list(request):
    movies = Movie.objects.all()

    context = {
        'movies': movies,
        'title': 'Афиша'
    }

    return render(
        request,
        'cinema/movie_list.html',
        context
    )