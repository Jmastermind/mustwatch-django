from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from mixer.backend.django import mixer

from movies.models import Movie, UserMovie

User = get_user_model()


class MoviesViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.movies = mixer.cycle(20).blend(Movie)
        cls.user = mixer.blend(User)
        cls.favorites = mixer.cycle(5).blend(
            UserMovie,
            user=cls.user,
            movie=(cls.movies[i] for i in range(6)),
        )

    def test_something(self) -> None:
        # print([i[0] for i in Movie.objects.only('pk').values_list('pk')])
        # print(Movie.objects.filter(viewers=get_user_model().pk).exists())
        print(self.user.films.first().pk)
