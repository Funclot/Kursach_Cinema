from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Movie, Session, Ticket

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
@login_required
def buy_ticket(request, session_id):

    session = get_object_or_404(
        Session,
        pk=session_id
    )

    if request.method == 'POST':

        seat_number = request.POST.get(
            'seat_number'
        )

        Ticket.objects.create(
            user=request.user,
            session=session,
            seat_number=seat_number
        )

        return redirect('/')

    context = {
        'session': session
    }

    return render(
        request,
        'cinema/buy_ticket.html',
        context
    )

@login_required
def my_tickets(request):

    tickets = Ticket.objects.filter(
        user=request.user
    ).order_by('-purchase_date')

    context = {
        'tickets': tickets
    }

    return render(
        request,
        'cinema/my_tickets.html',
        context
    )
def session_list(request):

    sessions = Session.objects.select_related(
        'movie'
    ).order_by('start_time')

    context = {
        'sessions': sessions
    }

    return render(
        request,
        'cinema/session_list.html',
        context
    )