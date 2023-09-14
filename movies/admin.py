from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from movies.models import Movie, UserMovie


class MovieAdmin(TranslationAdmin):
    list_display = ('title', 'poster')
    search_fields = ('title',)
    list_filter = ('title', 'year')


admin.site.register(Movie, MovieAdmin)


@admin.register(UserMovie)
class UserMovieAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie')
    search_fields = ('user',)
    list_filter = ('movie',)
