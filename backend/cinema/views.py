from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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

    sessions = movie.sessions.filter(
        start_time__gte=timezone.now()
    )

    context = {
        'movie': movie,
        'sessions': sessions,
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

        ticket_exists = Ticket.objects.filter(
            session=session,
            seat_number=seat_number
        ).exists()

        if ticket_exists:
            context = {
                'session': session,
                'error': 'Это место уже занято.'
            }

            return render(
                request,
                'cinema/buy_ticket.html',
                context
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
        user=request.user,
        session__start_time__gte=timezone.now()
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

    selected_date = request.GET.get('date')

    future_sessions = Session.objects.filter(
        start_time__gte=timezone.now()
    ).order_by('start_time')

    first_session = future_sessions.first()

    nearest_date = None

    if first_session:
        nearest_date = first_session.start_time.date()

    if selected_date:

        sessions = Session.objects.select_related(
            'movie'
        ).filter(
            start_time__date=selected_date
        ).order_by('start_time')

    else:

        sessions = future_sessions

    context = {
        'sessions': sessions,
        'selected_date': selected_date,
        'nearest_date': nearest_date
    }

    return render(
        request,
        'cinema/session_list.html',
        context
    )

@login_required
def cancel_ticket(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        pk=ticket_id,
        user=request.user
    )

    ticket.delete()

    return redirect('my_tickets')