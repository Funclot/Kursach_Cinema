from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    release_date = models.DateField()

    is_active = models.BooleanField(default=True)

    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='movies'
    )

    poster = models.ImageField(
        upload_to='posters/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class Session(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='sessions'
    )

    start_time = models.DateTimeField()
    hall = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.movie.title} - {self.start_time}'


class Ticket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    seat_number = models.PositiveIntegerField()

    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.session}'