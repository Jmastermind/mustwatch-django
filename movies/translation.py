from modeltranslation.translator import TranslationOptions, translator

from movies.models import Movie


# for Person model
class MovieTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'type',
        'genre',
        'director_1',
        'director_2',
        'star_1',
        'star_2',
        'star_3',
        'description',
    )
    empty_values = ''
    required_languages = ('ru',)
    fallback_undefined = ''
    empty_values = {'director_2_ru': ''}


translator.register(Movie, MovieTranslationOptions)
