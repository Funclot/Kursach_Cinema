from django.shortcuts import render, get_object_or_404
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

def movie_detail(request, movie_id):
    movie = get_object_or_404(
        Movie,
        pk=movie_id
    )

    context = {
        'movie': movie
    }

    return render(
        request,
        'cinema/movie_detail.html',
        context
    )