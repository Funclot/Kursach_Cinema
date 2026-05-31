from django.urls import path
from .views import (
    movie_list,
    movie_detail,
    buy_ticket,
)

urlpatterns = [
    path('', movie_list, name='movie_list'),

    path(
        'movie/<int:movie_id>/',
        movie_detail,
        name='movie_detail'
    ),

    path(
        'session/<int:session_id>/buy/',
        buy_ticket,
        name='buy_ticket'
    ),
]