from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView

from movies import views

app_name = '%(app_label)s'

urlpatterns = [
    path('', views.MoviesHome.as_view(), name='home'),
    path('movies/<int:pk>', views.MoviesView.as_view(), name='movie'),
    path('watchlist/', views.WatchlistView.as_view(), name='watchlist'),
    path(
        'watchlist/<int:pk>',
        views.WatchlistMovie.as_view(),
        name='watchlist_movie',
    ),
    path(
        'watchlist/<int:pk>/manage/',
        views.WatchlistManage.as_view(),
        name='watchlist_manage',
    ),
]
