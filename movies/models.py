from django.contrib.auth import get_user_model
from django.db import models


class Movie(models.Model):
    """ORM containing movie data."""

    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    genre = models.CharField(max_length=50)
    director_1 = models.CharField(max_length=50)
    director_2 = models.CharField(max_length=50, blank=True)
    star_1 = models.CharField(max_length=50, blank=True)
    star_2 = models.CharField(max_length=50, blank=True)
    star_3 = models.CharField(max_length=50, blank=True)
    kp = models.DecimalField(max_digits=2, decimal_places=1)
    imdb = models.DecimalField(max_digits=2, decimal_places=1)
    description = models.TextField(max_length=185)
    poster = models.ImageField(
        upload_to='posters/',
        blank=True,
        default='posters/noposter.png',
    )
    watched = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'year', 'director_1'],
                name='unique_movie',
            ),
        ]

    def __str__(self) -> str:
        super().__str__()
        return self.title


class UserMovie(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='films',
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='viewers',
    )

    def __str__(self) -> str:
        super().__str__()
        return f'`{self.user.username}` watches `{self.movie.title}` movie.'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'movie'],
                name='unique_user_movie',
            ),
        ]
