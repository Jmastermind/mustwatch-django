from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView

from movies import models


class MoviesHome(TemplateView):
    template_name = 'movies/movies.html'

    def get(self, request, *args, **kwargs):
        del request, args
        context = self.get_context_data(**kwargs)
        if models.Movie.objects.exists():
            return redirect(
                'movies:movie',
                pk=models.Movie.objects.first().pk,
            )
        return self.render_to_response(context)


class WatchlistView(LoginRequiredMixin, TemplateView):
    template_name = 'movies/movies.html'

    def get(self, request, *args, **kwargs) -> HttpResponse:
        del args
        user = get_user_model().objects.get(pk=request.user.pk)
        context = self.get_context_data(**kwargs)
        if self.request.user.films.exists():
            return redirect(
                'movies:watchlist_movie',
                pk=user.films.first().movie.pk,
            )
        return self.render_to_response(context)


class MoviesView(TemplateView):
    template_name = 'movies/movies.html'

    def get(self, request, *args, **kwargs) -> HttpResponse:
        del args
        context = self.get_context_data(**kwargs)
        movie_pk = kwargs.get('pk')
        context['many'] = models.Movie.objects.count() > 1
        context['movie'] = get_object_or_404(models.Movie, pk=movie_pk)
        movies_list = [
            i[0]
            for i in models.Movie.objects.only('pk')
            .order_by('pk')
            .values_list('pk')
        ]
        cur = movies_list.index(movie_pk)
        context['next'] = (
            movies_list[cur + 1]
            if cur + 1 < len(movies_list)
            else movies_list[0]
        )
        context['previous'] = (
            movies_list[cur - 1] if cur - 1 >= 0 else movies_list[-1]
        )
        if request.user.is_authenticated:
            context['in_watchlist'] = (
                context['movie'].viewers.filter(user=request.user.pk).exists()
            )
        return self.render_to_response(context)


class WatchlistMovie(LoginRequiredMixin, TemplateView):
    template_name = 'movies/movies.html'

    def get(self, request, *args, **kwargs) -> HttpResponse:
        del args
        movie_pk = kwargs.get('pk')
        context = self.get_context_data(**kwargs)
        context['movie'] = get_object_or_404(models.Movie, pk=movie_pk)
        movies_list = [
            i[0]
            for i in request.user.films.only('movie__pk').values_list(
                'movie__pk',
            )
        ]
        cur = movies_list.index(movie_pk)
        context['next'] = (
            movies_list[cur + 1]
            if cur + 1 < len(movies_list)
            else movies_list[0]
        )
        context['previous'] = (
            movies_list[cur - 1] if cur - 1 >= 0 else movies_list[-1]
        )
        context['in_watchlist'] = True
        context['many'] = request.user.films.count() > 1
        return self.render_to_response(context)


class WatchlistManage(LoginRequiredMixin, TemplateView):
    template_name = 'movies/movies.html'

    def get(self, request, *args, **kwargs) -> HttpResponseRedirect:
        del args
        movie = get_object_or_404(models.Movie, pk=kwargs.get('pk'))
        if movie.viewers.filter(user=request.user.pk).exists():
            models.UserMovie.objects.filter(
                user=request.user,
                movie=movie,
            ).delete()
        else:
            models.UserMovie.objects.create(
                user=request.user,
                movie=movie,
            )
        if request.META.get('HTTP_REFERER').split('/')[-2] == 'watchlist':
            return redirect('movies:watchlist')
        return redirect('movies:movie', kwargs.get('pk'))
