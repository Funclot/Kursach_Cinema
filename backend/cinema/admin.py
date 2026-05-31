from django.contrib import admin
from .models import Genre, Movie, Session, Ticket


admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Session)
admin.site.register(Ticket)